# FqQuAD_Question_Context

Here is a overview of possible approches:

## Tokenizing words and sentences

* Use of "NTLK" package and "gensim"
* Use of "gensim" Dictionary and Similarity functions
* main.py returns the appriorate to a random selected question, ie. the context 

## Metrics used 

To find out if the context ouput is the right one:
* a function, checks in the train.json file, it is the appropriate context. 
- if yes : return 1
- else : return 0

If 0 is retured, we loook at the top 3 possible 

Performances over a set of 100 random questions :
- 46% of questions were given the right context
- for 53% of questions, top 3 similar contexts returned 


## Other possible approaches

### More efficient approches

* Bert tokenzing + classification
* Use LSTM 