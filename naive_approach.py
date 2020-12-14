import numpy
from data.data_import import *

path='train.json'

question=select_question(path)
list_contexts=import_context(path)

def similarity(question, context):
    intersection = set(question).intersection(set(context))
    union = set(question).union(set(context))
    return len(intersection)/len(union)


most_similar=[]
rate=0

for c in list_contexts:
    current_rate=similarity(question,c)
    if(current_rate>rate):
        most_similar=c
        rate=current_rate
print("Question : ",question)
print("Context: ",most_similar)