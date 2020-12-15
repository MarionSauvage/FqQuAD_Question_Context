from data.data_import import *
from model.tokenize_questions import *
from model.tokenize_context import *
from gensim.corpora import Dictionary
from gensim.similarities import Similarity
from metrics import *

import argparse
from gensim.test.utils import get_tmpfile

def main(path="train.json"):
    #get a random question
    quest=select_question(path)
    print("Random question : ")
    print(quest)
    #Tokenize and create gensim dictionnary
    dictionary,corpus_quest=process_question(quest)
    tfidf=gensim.models.TfidfModel(corpus_quest)
    #corpus of contexts processing
    ctx=import_context(path)
    corpus=process_contexts(ctx) 
    #Global corpus dictionnary 
    corpus=final_process_context(corpus,dictionary)
    dir_for_index=get_tmpfile("index_sim")
    #Similarity function to compare each context to the question
    sim=Similarity(dir_for_index,corpus,num_features=len(dictionary))
    #result list of similarity scores
    res=(sim[corpus_quest].tolist()[0])

    #Get 3 best most similar context from result list
    max_index = sorted(range(len(res)), key = lambda sub: res[sub])[-3:] 
    #create dict of index (to be able able to find the context in the context list) and similarity value 
    dict_best={}
    for e in max_index:
        dict_best[e]=res[e]
    #get index of best falue
    best_index=max(dict_best,key=dict_best.get)
    print("Best context")
    print(ctx[best_index])
    #use function sim_metric to find out if it is the appropriate context (it will return 1)
    sim_accuracy=sim_metric(quest,ctx[best_index])
    print("similarity metric",sim_accuracy)

    #Look for other good solutions if the first option is not satisfactory
    #top3metric tells if there is a adequate solution in the 3 most similar context returned 
    #if the first example was a good fit , it will automatically return 1 
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
    #it returns the best context if it as adequate
    #or 2 other possible contexts if the first output is not right


    # result_top1=[]
    # result_top3=[]main
    # for i in range(100):
    #     res=main()
    #     result_top1.append(res[0])
    #     result_top3.append(res[1])
    # print(sum(result_top1)/len(result_top1)*100,"%")
    # print(sum(result_top3)/len(result_top3)*100,"%")





