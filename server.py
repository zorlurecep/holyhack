import eel
import time
import imdb_scraper
from data import Data

eel.init('web')


def get_genres(data, movie_ids):
    all_genres = set()
    for current_id in movie_ids:
        genres = set(data.df[data.df.tconst == current_id].genres)
        all_genres.update(genres)
    genres = { genre for string in genres for genre in string.split(',')}

    return list(genres)

def search_by_name(data, movie_name, content_type, year):
    """
    :param data: panda dataframe
    :param movie_name: string
    :return: None if movie_name illegal,
             (empty) set of tags if movie_name legal
    """
    if data.df[data.df.originalTitle == movie_name].empty:
        return None

    movie_ids = data.title_to_id(movie_name, content_type, year)
    tags = set()
    i = 1
    for movie_id in movie_ids:
        if i > 15:
            break
        print(movie_id, str(i) + 'th reference to', movie_name)
        i += 1
        tags.update(imdb_scraper.get_keywords_from_id(movie_id))

    tags = list(tags)
    tags.sort(reverse=True)
    tags = [elm[1] for elm in tags]

    tags = get_genres(data, movie_name) + tags
    return tags


@eel.expose
def search(movie_name, keyword, content_type, year):
    # year = None
    # content_type = 'movie'
    movie_name = movie_name.upper()
    content_type = content_type.upper()
    if keyword is None:
        print(movie_name, keyword, content_type, year)
        tags = search_by_name(data, movie_name, content_type, year)

        print("\nTags related to " + movie_name + " are: \n", tags)
        return tags


if __name__ == "__main__":
    data = Data()
    eel.start('main.html', mode="chrome-app", host="localhost", port=8080)
