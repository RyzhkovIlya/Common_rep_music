import os
from dotenv import load_dotenv
# from joblib import Parallel, delayed

load_dotenv()
API_TOKEN = os.getenv('TOKEN_GENIUS')

def get_lyrics(name, k):
    c = 0
    import lyricsgenius as lg
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
        response = genius.search_artist(name, max_songs=k, sort='popularity')
        songs = response.songs
        s = [song.lyrics for song in songs]
        name_1 = response.name

        with open(f"api/database/raw_data/{name_1}.txt", "w") as f:
            f.write('\n \n'.join(s))
        c += 1
        print(f"Songs grabbed:{len(s)}")
    except:
        print(f"some exception at {name}: {c}")

def pars(name):
    return get_lyrics(name, 20)