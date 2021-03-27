from imdb_scraper import *
from data import *


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
    for movie_id in movie_ids:
        print(movie_id)
        tags.update(get_keywords_from_id(movie_id))
    return tags


if __name__ == "__main__":
    #get_movies_form_keyword("crime-family")
    t1 = time.time()
    data = Data()

    movie_name = "The Godfather"
    tags_of_movie = search_by_name(data, movie_name)
    print(tags_of_movie)

    t2 = time.time()
    print(t2 - t1)
