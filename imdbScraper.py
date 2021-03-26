import requests
from bs4 import BeautifulSoup


def get_page_content(movie_id):
    return requests.get("https://www.imdb.com/title/" + movie_id + "/keywords").content


def scrape_page_content(movie_name, page_content, movie_keyword, keyword_movie):
    soup = BeautifulSoup(page_content, 'html.parser')
    all_tags = soup.find_all("div", {"class": "sodatext"})

    return add_to_movie_keyword_dictionary(movie_name, all_tags, movie_keyword, keyword_movie)


def add_to_movie_keyword_dictionary(movie_name, all_tags, movie_keyword, keyword_movie):
    if movie_name not in movie_keyword:
        movie_keyword[movie_name] = []

    for tag in all_tags:
        current_keyword = tag.text.strip("\n")
        if current_keyword not in movie_keyword[movie_name]:
            movie_keyword[movie_name].append(current_keyword)
            keyword_movie = add_to_keyword_movie_dictionary(movie_name, current_keyword, keyword_movie)

    return movie_keyword, keyword_movie


def add_to_keyword_movie_dictionary(movie_name, current_keyword, keyword_movie):
    if current_keyword not in keyword_movie:
        keyword_movie[current_keyword] = []

    if movie_name not in keyword_movie[current_keyword]:
        keyword_movie[current_keyword].append(movie_name)

    return keyword_movie
