import eel
import time
import imdb_scraper
from data import Data

eel.init('web')


def search_by_name(data, movie_name):
    """
    :param data: panda dataframe
    :param movie_name: string
    :return: None if movie_name illegal,
             (empty) set of tags if movie_name legal
    """
    if data.df[data.df.originalTitle == movie_name].empty:
        return None
    movie_ids = data.title_to_id(movie_name)
    tags = set()
    i = 1
    for movie_id in movie_ids:
        print(str(i) +'th reference to', movie_id)
        i += 1
        tags.update(imdb_scraper.get_keywords_from_id(movie_id))
    return tags


@eel.expose
def search(movieName, keywordName, contentType, year):
    if keywordName is None:
        print(movieName, keywordName, contentType, year)
        tags = search_by_name(data, movieName)
        print("\nTags are: \n", tags)


if __name__ == "__main__":
    data = Data()
    eel.start('main.html', mode="chrome-app", host="localhost", port=8080)
