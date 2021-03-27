import requests
from bs4 import BeautifulSoup


def get_page_content_keywords(keyword, page_number):
    if page_number is None:
        return requests.get("https://www.imdb.com/search/keyword/?keywords=" + keyword).content
    else:
        return requests.get("https://www.imdb.com/search/keyword/?keywords=" + keyword + "&page=" + page_number).content


def get_keywords_from_id(movie_id):
    """
    :param movie_id: (string) legal movie id
    :return: set of tags
    """
    page_content = requests.get("https://www.imdb.com/title/" + movie_id + "/keywords").content
    soup = BeautifulSoup(page_content, 'html.parser')
    all_tags = soup.find_all("div", {"class": "sodatext"})

    relevancy_of_keyword = soup.find_all("div", {"class": "interesting-count-text"})

    keywords = set()
    for tag in all_tags:
        current_keyword = tag.text.strip("\n")
        keywords.add(current_keyword)
    return keywords


def get_movies_form_keyword(keyword):
    page_content = get_page_content_keywords(keyword, None)
    soup = BeautifulSoup(page_content, 'html.parser')
    all_movies = soup.find_all("div", {"class": "lister-item mode-detail"})

    movies = set()
    for movie in all_movies:
        movies.add(movie.find_all("a")[1].text)

    i = 2
    while True:
        error_message = "No results. Try removing genres, ratings, or other filters to see more."
        page_content = get_page_content_keywords(keyword, 2)
        soup = BeautifulSoup(page_content, 'html.parser')
        all_movies = soup.find_all(error_message)

        for movie in all_movies:
            movies.add(movie.find_all("a")[1].text)

        i += 1



