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
sim=Similarity('../workdir',tfidf[corpus_quest],num_features=len(dictionary))
query_ctx=tfidf[corpus]
print(len(sim[query_ctx]))
print((sim[query_ctx]))