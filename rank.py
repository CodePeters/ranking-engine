#!/usr/local/bin/python3
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import preprocess

def tfidf_scores(corpus, query):
	cv=CountVectorizer(max_df=0.85)
	word_count_vector=cv.fit_transform(corpus)
	tfidf_transformer=TfidfTransformer(smooth_idf=True, use_idf=True, norm=None)
	tfidf = tfidf_transformer.fit_transform(word_count_vector)
	tfidf_array = tfidf.toarray()
	scores = np.zeros( len(abstract))

	for q in query:
		if(q in cv.vocabulary_ ):
			scores += tfidf_array[:,cv.vocabulary_.get(q)]
	return scores


if __name__ == "__main__":

	fileName = "out_file.txt" 
	query = input()    
	N = 10  
	alpha = 0.4         
	data,abstract,keywords,title = ([] for _ in range(4))

	for line in open(fileName,'r', encoding='utf8'):
		data.append(json.loads(line))
		abstract.append(data[-1]['abstract'])
		keywords.append(data[-1]['keywords'])
		title.append(data[-1]['title'])

	query = preprocess.dataPreProcess(query)
	scores = np.zeros( len(abstract))
	scores += alpha*tfidf_scores(title, query)
	scores += ((1-alpha) / 2)*tfidf_scores(abstract, query)
	scores += ((1-alpha) / 2)*tfidf_scores(keywords, query)
	scores = scores.tolist()
	scores = list(zip(scores, range(len(scores))))
	scores.sort(reverse=True)

	for elem in  scores[:N]:
		index = elem[1]
		if(data[index]['titleCopy'] != ""): print("Text title:", data[index]['titleCopy'], " Text number:", index)
		else: print("This text has no title, text number:", index)
		