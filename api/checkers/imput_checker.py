import lyricsgenius as lg
def input_checker(name, API_TOKEN):
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, remove_section_headers=True)
        response = (genius.search_artist(name, max_songs=1, sort='popularity'))
        true_name = response.name
        return true_name
    except:
        return name