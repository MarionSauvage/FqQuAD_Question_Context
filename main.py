from data.data_import import *
from model.tokenize_questions import *
from gensim.corpora import Dictionary
from gensim.similarities import Similarity
from metrics import *

quest=select_question("train.json")
print(quest)
dictionary,corpus_quest=process_question(quest)
tfidf=gensim.models.TfidfModel(corpus_quest)

ctx=import_context("train.json")
corpus=process_contexts2(ctx) 
corpus=final_process_context(corpus,dictionary)
sim=Similarity('../workdir',corpus,num_features=len(corpus))
res=(sim[corpus_quest].tolist()[0])

max_index = sorted(range(len(res)), key = lambda sub: res[sub])[-5:] 
dict_best={}
for e in max_index:
    dict_best[e]=res[e]
best_index=max(dict_best,key=dict_best.get)
print(ctx[best_index])

print("similarity metric",sim_metric(quest,ctx[best_index]))

#recherche d'autres solutions de score égaux
max_val=max(dict_best)
other_solutions_index=[]
for j, value in dict_best.items():
    if(j!=best_index and value==max_val):
        other_solutions_index.append(j)
if len(other_solutions_index)!=0:
    print("Autres solutions possibles")
    for k in other_solutions_index:
        print(sim_metric(quest,ctx[k]))
        print(ctx[k])

# i=1
# for k in max_index:
#     print("Context "+str(i)+" avec un score égal à : "+str(dict_best[k]))
#     print(ctx[k]) 
#     i+=1





