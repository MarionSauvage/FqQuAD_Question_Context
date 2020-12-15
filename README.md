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


## Other possible approaches

### Naïve approach 

* jaquard similarity

### More efficient approches

* Bert tokenzing + classification
* Use LSTM 