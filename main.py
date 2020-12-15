from data.data_import import *
from model.tokenize_questions import *
from gensim.corpora import Dictionary
from gensim.similarities import Similarity

quest=select_question("train.json")
print(quest)
dictionary,corpus_quest=process_question(quest)
tfidf=gensim.models.TfidfModel(corpus_quest)

ctx=import_context("train.json")
corpus=process_contexts2(ctx)
corpus=final_process_context(corpus,dictionary)
sim=Similarity('../workdir',corpus,num_features=len(dictionary))
res=(sim[corpus_quest].tolist()[0])

max_index = sorted(range(len(res)), key = lambda sub: res[sub])[-10:] 
print(max_index)

for i in range(len(max_index)):
    print("Context "+str(i+1))
    print(ctx[i])


