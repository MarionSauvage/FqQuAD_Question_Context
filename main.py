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
print(type(sim[corpus_quest]))
res=(sim[corpus_quest].tolist()[0])
best=max(res)

#print(res)
best_scores=[0,0,0]
max_index=[0,1,2]
#Return 3 most possible contexts
for i,score in enumerate(res):
    if score > best_scores[0]:
        best_scores[0]=score
        max_index[0]=i
        pass
    elif(score > best_scores[1]):
        best_scores[1]=score
        max_index[1]=i
        pass
    elif(score > best_scores[2]):
        best_scores[2]=score
        max_index[2]=i
        pass
    else:
        pass
print(max_index)
print(best_scores)

for k in max_index:
    print(ctx[k])
