import os
from api.core.cleaner import clean_lemm_general
from api.checkers.name_checker import name_checker
from api.checkers.input_checker import input_checker
from api.loader import API_TOKEN
import pickle
from musicmatcher import tfidf
import pandas as pd
for i in os.listdir('../api/database/raw_data'):
    os.rename(f'../api/database/raw_data/{i}', f'../api/database/raw_data/{name_checker(i[:-4], API_TOKEN)}.txt')

tfidf_not_exists = 'TF_IDF.csv' not in os.listdir('../api/database')
print(tfidf_not_exists)
if tfidf_not_exists:
    dictionary_words = {}
    for i in os.listdir('../api/database/raw_data'):
        try:
            with open(f'../api/database/raw_data/{i}', encoding='utf-8', newline='') as f:
                artist_text = f.read()
                dictionary_words[i[:-4]] = clean_lemm_general(artist_text)
        except:
            print(i)
    pickle.dump(dictionary_words, open("../api/database/dictionary_words.pickle", "wb"))
    artists_similarity = tfidf(pickle.load(open("../api/database/dictionary_words.pickle", 'rb')))
    pd.DataFrame(artists_similarity, index=dictionary_words.keys()).to_csv('../api/database/TF_IDF.csv')

name = 'Muse'
name = input_checker(name)
name = name_checker(name, API_TOKEN)

df = pd.read_csv('../api/database/artist_names.csv')
if name in df['authors'].to_list():
    df_TF_IDF = pd.read_csv('../api/database/TF_IDF.csv', index_col=0)
    print('\n'.join(*[df_TF_IDF['Muse'].sort_values(ascending=False).head(6)[1:].index.to_list()]))

