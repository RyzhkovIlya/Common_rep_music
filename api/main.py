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

try:
    pd.read_csv('../api/database/TF_IDF.csv')
    print('Done')
except:
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
    pd.DataFrame(artists_similarity, columns=dictionary_words.keys(), index=dictionary_words.keys()).to_csv('../api/database/TF_IDF.csv', )

name = 'Muse'
name = input_checker(name)
name = name_checker(name, API_TOKEN)
if name in pd.read_csv('../api/database/artist_names.csv'):
    df = pd.read_csv('../api/database/artist_names.csv')
    print(',\n'.join([df[name].sort_values(ascending=False).index[1:6]]))
