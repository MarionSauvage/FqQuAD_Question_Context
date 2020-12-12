import json
import pandas as pd 
import numpy as np 


path="train.json"
with open(path,'r',encoding='utf-8') as f:
    data = json.loads(f.read()) 
# Normalizing data
multiple_level_data = pd.json_normalize(data.get('data'),['paragraphs'],'title')
df_paragraphs = pd.json_normalize(data.get('data'),["paragraphs","qas"],["paragraphs",'title'])
multiple_level_data=pd.DataFrame(multiple_level_data)
df_global=pd.merge(df_paragraphs,multiple_level_data,on='title')
print(df_global.sample())
