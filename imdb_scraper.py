# import requests
# from bs4 import BeautifulSoup
#
#
# def get_page_content(movie_id):
#     return requests.get("https://www.imdb.com/title/" + movie_id + "/keywords").content
#
#
# # def get_page_content_keywords(keyword, page_number):
# #     if page_number is None:
# #         return requests.get("https://www.imdb.com/search/keyword/?keywords=", keyword)
# #     else:
# #         return requests.get("https://www.imdb.com/search/keyword/?keywords=" + keyword + "&page=" + page_number)
# #
#
# def get_keywords_from_id(movie_id):
#     """
#     :param movie_id: (string) legal movie id
#     :return: set of tags
#     """
#     page_content = requests.get("https://www.imdb.com/title/" + movie_id + "/keywords").content
#     soup = BeautifulSoup(page_content, 'html.parser')
#     all_tags = soup.find_all("div", {"class": "sodatext"})
#
#     relevancy_of_keyword = soup.find_all("div", {"class": "interesting-count-text"})
#
#     keywords = set()
#     for tag in all_tags:
#         current_keyword = tag.text.strip("\n")
#         keywords.add(current_keyword)
#     return keywords
#
#
# #def get_movies_form_keyword
#
#     # return add_to_movie_to_keyword_dictionary(movie_name, all_tags, movie_to_keyword, keyword_to_movie)
#
# # def add_to_movie_to_keyword_dictionary(movie_name, all_tags, keywords):
# #     for tag in all_tags:
# #         current_keyword = tag.text.strip("\n")
# #         keywords[movie_name].add(current_keyword)
# #
# #     return keywords
#
#
# # def add_to_keyword_to_movie_dictionary(movie_name, keyword, keyword_to_movie):
# #     if keyword not in keyword_to_movie:
# #         keyword_to_movie[keyword] = set()
# #
# #     keyword_to_movie[keyword].add(movie_name)
# #
# #     # return keyword_to_movie


import requests
from bs4 import BeautifulSoup


# def get_page_content_keywords(keyword, page_number):
#     if page_number is None:
#         return requests.get("https://www.imdb.com/search/keyword/?keywords=", keyword)
#     else:
#         return requests.get("https://www.imdb.com/search/keyword/?keywords=" + keyword + "&page=" + page_number)
#

def get_keywords_from_id(movie_id):
    """
    :param movie_id: (string) legal movie id
    :return: set of tuples each containing a tag and its relevance
    """
    page_content = requests.get("https://www.imdb.com/title/" + movie_id + "/keywords").content
    soup = BeautifulSoup(page_content, 'html.parser')
    all_tags = soup.find_all("div", {"class": "sodatext"})

    relevancy_of_keyword = soup.find_all("div", {"class": "interesting-count-text"})

    keywords = set()
    for tag, relevancy in zip(all_tags, relevancy_of_keyword):
        current_keyword = tag.text.strip("\n")
        current_relevancy = relevancy.text.strip("\n")
        current_relevancy = current_relevancy[1:-1]
        if current_relevancy[0] == "I":
            relevance = 0
        else:
            relevance = int(current_relevancy[0])

        keywords.add((relevance, current_keyword))
    return keywords