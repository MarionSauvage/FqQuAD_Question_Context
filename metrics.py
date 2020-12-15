import json
import pandas as pd 
import numpy as np 
import random


with open("./train.json",'r',encoding='utf-8') as f:
        data = json.loads(f.read())
multiple_level_data = pd.json_normalize(data.get('data'),['paragraphs'],'title')
multiple_level_data=pd.DataFrame(multiple_level_data)
df_paragraphs = pd.json_normalize(data.get('data'),["paragraphs","qas"],["paragraphs",'title'])
df_global=pd.merge(df_paragraphs,multiple_level_data,on='title')

def sim_metric(question,context):
    df_reduced=df_global[df_global["question"]==question]
    list_ctx=list(df_reduced["context"])
    if context in list_ctx:
        return 1
    else:
        return 0