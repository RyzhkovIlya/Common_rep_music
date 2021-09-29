import lyricsgenius as lg
from joblib import Parallel, delayed

def name_checker(names):
    res = []
    for i in names:
        try:
            genius = lg.Genius(API_TOKEN, skip_non_songs=True, remove_section_headers=True)
            name = (genius.search_artist(i, max_songs=1, allow_name_change=True)).name
            res.append(name)
        except:
            print('error')
    Parallel(n_jobs=20, verbose=1)(delayed(name_checker)(i) for i in names)

    return res