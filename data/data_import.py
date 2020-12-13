import json
import pandas as pd 
import numpy as np 
import random
path="train.json"

def import_context(path_context):
    with open(path,'r',encoding='utf-8') as f:
        data = json.loads(f.read()) 
    # Normalizing data
    multiple_level_data = pd.json_normalize(data.get('data'),['paragraphs'],'title')
    multiple_level_data=pd.DataFrame(multiple_level_data)
    list_contexts=list(multiple_level_data['context'])
    return list_contexts

def select_question(path_question):
    with open(path,'r',encoding='utf-8') as f:
        data = json.loads(f.read()) 
    # Normalizing data
    df_paragraphs = pd.json_normalize(data.get('data'),["paragraphs","qas"],["paragraphs",'title'])
    liste_questions=list(df_paragraphs['questions'])
    random_quest=random.randint(0,len(liste_questions))
    return liste_questions[random_quest]
