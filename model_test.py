import os
import nltk
from dotenv import load_dotenv
from api.musicmatcher import final_df
nltk.download('stopwords')
load_dotenv()
API_TOKEN = os.getenv('TOKEN_GENIUS')

def similar_artist(artist_name, dict_of_artist_similary, text_dict):

    # text_dict = read_text(API_TOKEN)
    #
    # artists_similarity = tfidf(text_dict)
    #
    # dict_of_artist_similary = dict(zip(text_dict.keys(), artists_similarity))

    return final_df(artist_name, dict_of_artist_similary, text_dict)