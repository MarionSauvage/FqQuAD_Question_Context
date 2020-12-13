from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
import gensim
nltk.download('punkt')
import numpy
import random

def process_question(question):
    tok_quest=sent_tokenize(question)
    gen_docs=[]
    for line in tok_quest: #often more than tokenized sentenced per context
        for word in word_tokenize(line):
            gen_docs.append(word.lower())
    #make it a list of list
    l=[]
    l.append(gen_docs)
    gen_docs=l
    dictionary=gensim.corpora.Dictionary(gen_docs)
    print(dictionary.token2id)
    corpus=[dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    print(corpus)
    tfidf=gensim.models.TfidfModel(corpus)
    return tfidf

question="Comment vas tu ? "

print(process_question(question))

def process_contexts(context_list):
    tokenized_sentenced_context=[]
    for ctxt in list_contextes:
        tokenized_sentenced_context.append(sent_tokenize(ctxt))
        dict_context={}
        for index,text in enumerate(tokenized_sentenced_context):
            gen_docs=[]
            for line in text: #often more than tokenized sentenced per context
                for word in word_tokenize(line):
                    if(word.lower() not in list_mots_vides)==True:
                        gen_docs.append(word.lower())
                        dict_context[index]=gen_docs
    