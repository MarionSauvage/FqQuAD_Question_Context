# FqQuAD Question/Context

Goal : for an random question return adequate context

Dataset used : FqQuAD https://fquad.illuin.tech/

Here is an overview of possible approaches:

## Tokenizing words and sentences

* Use of "NTLK" package and "gensim"
* Use of "gensim" Dictionary and Similarity functions
* main.py returns the appriorate context to a random selected question, ie. the context with the best similarity score (gensim similiarity)
* if it doesn't return the right context, it returns the 2 next possible options

## Metrics used 

To find out if the context ouput is the right one:
* a function, checks in the train.json file, it is the appropriate context. 
- if yes : return 1
- else : return 0

If 0 is retured, we loook at the top 3 possible 

Performances over a set of 100 random questions :
- 46% of questions were given the right context
- for 53% of questions, top 3 similar contexts returned 

<i> CLI execution </i> : python main.py -path "train.json"

CLI argument : -path (indicate FqQuAD json file location) default "train.json"


## Other possible approaches

### More efficient approches

* Bert tokenzing + classification
* Use LSTM 