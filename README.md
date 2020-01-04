# ranking-engine [![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/CodePeters/Pacman/blob/master/LICENSE)

**A ranking engine for text search. Given a query and a set of articles, it returns N most relevant articles. 

## Input
The input required is a file ("file.txt") with the articles in json format:

`
{"abstract":"The article text here!!!",
 "keywords":["keyword1", "keyword2.. etc"],
 "title":"The title here"} `
 
It may have more fields which will be ignored, also if one of the fields above is missing algorithms ignores it in computations. 

## Execution

* First run preprocess.py which does some preprocess to the articles and produces an output file. 

* Then run rank.py which takes as input the previous generated file and a query from standard input and using tf-idf it returns N most relevant articles. The ranking also gives diferrent weights to the article's abstract, keywords and title.



## _License_

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
