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
