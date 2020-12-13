from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
import gensim
nltk.download('punkt')

def process_question(question):
    tok_quest=sent_tokenize(question)
    

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
    