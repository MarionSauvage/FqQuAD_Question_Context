from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import gensim
nltk.download('punkt')
import numpy
import random
from gensim.corpora import Dictionary

#mots vides en français 
stop_words=set(stopwords.words('french'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) 


def process_question(question):
    print(question)
    tok_quest=sent_tokenize(question)
    question=[[word.lower() for word in word_tokenize(line) if word.lower() not in stop_words] for line in tok_quest ]
    dictionary=gensim.corpora.Dictionary(question)
    corpus=[dictionary.doc2bow(q) for q in question]
    return dictionary,corpus

# def process_contexts(context_list):
#     tokenized_sentenced_context=[]
#     for ctxt in context_list:
#         tokenized_sentenced_context.append(sent_tokenize(ctxt))
#     dict_context={}
#     for index,text in enumerate(tokenized_sentenced_context):
#         gen_docs=[]
#         for line in text: #often more than tokenized sentenced per context
#             for word in word_tokenize(line):
#                 gen_docs.append(word.lower())
#                 dict_context[index]=gen_docs
#     dict_context_id={}
#     for key,value in dict_context.items():
#         list_val=[]
#         list_val.append(value)
#         dictionary = gensim.corpora.Dictionary((list_val))
#         dict_context_id[key]=dictionary
#     dict_corpus={}
#     for key,value in dict_context.items():
#         dictionary=dict_context_id[key]
#         corpus=[]
#         #value is  a dict
#         dict_corpus[key]=dictionary.doc2bow(value)
#     return dict_corpus



def process_contexts2(context_list):
    tokenized_sentenced_context=[]
    for ctxt in context_list:
        tokenized_sentenced_context.append(sent_tokenize(ctxt))
    test=[[word.lower() for word in word_tokenize(text[0]) if word.lower() not in stop_words] for text in tokenized_sentenced_context]
    return test

def final_process_context(ctxt_token,dictionary):
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in ctxt_token]
    return corpus


    


def similarity_index(tfidf_corpus,dictionary):
    sims=gensim.similarities.Similarity('workdir/',tfidf_corpus,num_features=len(dictionary))

def find_similarities(tfidf,corpus_contextes):
    query_doc=tfidf[corpus_contextes]
    res=sims[query_doc]
    return res


