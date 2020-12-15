from data.data_import import *
from model.tokenize_questions import *
from gensim.corpora import Dictionary
from gensim.similarities import Similarity
from metrics import *

import argparse
from gensim.test.utils import get_tmpfile

def main(path="train.json"):
    quest=select_question(path)
    print(quest)
    dictionary,corpus_quest=process_question(quest)
    tfidf=gensim.models.TfidfModel(corpus_quest)
    #corpus of contexts processing
    ctx=import_context(path)
    corpus=process_contexts2(ctx) 
    corpus=final_process_context(corpus,dictionary)
    dir_for_index=get_tmpfile("index_sim")
    sim=Similarity(dir_for_index,corpus,num_features=len(dictionary))
    res=(sim[corpus_quest].tolist()[0])

    max_index = sorted(range(len(res)), key = lambda sub: res[sub])[-3:] 
    dict_best={}
    for e in max_index:
        dict_best[e]=res[e]
    best_index=max(dict_best,key=dict_best.get)
    #print(ctx[best_index])
    sim_accuracy=sim_metric(quest,ctx[best_index])
    print("similarity metric",sim_accuracy)

    #recherche d'autres solutions de score égaux
    top3metric=sim_accuracy
    if sim_accuracy==0:
        other_solutions_index=[]
        for j, value in dict_best.items():
            if(j!=best_index):
                other_solutions_index.append(j)
        if len(other_solutions_index)!=0:
            print("Autres solutions possibles")
            for k in other_solutions_index:
                #print(ctx[k])
                metric=sim_metric(quest,ctx[k])
                if(metric==1):
                    top3metric=1
                print("similarity metric",metric)
    
    return [sim_accuracy,top3metric]


if __name__=="__main__":
    my_parser=argparse.ArgumentParser(description="FqQuAD context finder")
    my_parser.add_argument("-path",default="train.json",help='Check that Fquad path is train.json or change default value')
    args=my_parser.parse_args()
    main(args.path)



    # result_top1=[]
    # result_top3=[]main
    # for i in range(100):
    #     res=main()
    #     result_top1.append(res[0])
    #     result_top3.append(res[1])
    # print(sum(result_top1)/len(result_top1)*100,"%")
    # print(sum(result_top3)/len(result_top3)*100,"%")





