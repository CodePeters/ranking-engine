#!/usr/local/bin/python3
import json
import string
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 

def flatten(list_of_lists):
	return [val for sublist in list_of_lists for val in sublist]

def stemming(data):
	ps = PorterStemmer()
	return [ps.stem(d) for d in data]

def tokeniz(data):
	return word_tokenize(data)

def removeStopwords(data):
	stop_words = set(stopwords.words('english'))
	return [d for d in data if not d in stop_words]

def removeNumbers(data):
	return [d.lower() for d in data if len(d)>1 and d.isalpha()]

def removePunctuation(data):
	translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
	return data.translate(translator)

def dataPreProcess(data):
	data = removePunctuation(data)
	data = tokeniz(data)
	data = removeNumbers(data) #also tolower and single words remove
	data = removeStopwords(data)
	data = stemming(data)
	return data

def JsondataPreProcess(JsonData):
	if(JsonData['abstract']): JsonData['abstract'] = dataPreProcess(JsonData['abstract'])
	else:  JsonData['abstract'] = ""
	if(JsonData['keywords']): JsonData['keywords'] = flatten(list(map(dataPreProcess, JsonData['keywords'])))
	else: JsonData['keywords'] = []
	if(JsonData['title']): JsonData['title'] = dataPreProcess(JsonData['title'])
	else: JsonData['title'] = JsonData['titleCopy'] = ""
	return JsonData

if __name__ == "__main__":

	fileName = "file.txt"  
	data = []

	for line in open(fileName,'r', encoding='utf8'):
		data.append(json.loads(line))
		data[-1]['titleCopy'] = data[-1]['title']
		if(data[-1]['keywords']): data[-1]['keywords'] = [i for i in data[-1]['keywords'] if i]

	data = list(map(JsondataPreProcess, data))

	with open("out_"+fileName, 'w') as outfile1:
		for jsonitem in data:
			dictionary = {}
			dictionary['abstract'] = " ".join(jsonitem['abstract'])
			dictionary['keywords'] = " ".join(jsonitem['keywords'])
			dictionary['title'] = " ".join(jsonitem['title'])
			dictionary['titleCopy'] = jsonitem['titleCopy']
			print(json.dumps(dictionary), file=outfile1)
