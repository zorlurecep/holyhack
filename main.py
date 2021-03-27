from imdbScraper import *
from pull_id_from_tsv import *


# def print_movie_to_keyword(max_to_print, movie_to_keyword):
#     print('\nPrinting movie_to_keyword..')
#     i = 1
#     for movie_title in movie_to_keyword:
#         print(movie_title)
#         i += 1
#         if i > max_to_print:
#             break
#
#
# def print_keyword_to_movie(max_to_print, keyword_to_movie):
#     print('\nPrinting keywordt_to_movie..')
#     i = 1
#     for keyword in keyword_to_movie:
#         print(keyword)
#         i += 1
#         if i > max_to_print:
#             break
#
#
# def create_dict_keyword_to_movie(data):
#     movie_to_keyword = {}
#     keyword_to_movie = {}
#     print('\nGetting the names and the years..')
#     t1 = time.time()
#     zipped = zip(data.df.tconst, data.get_extended_names())
#     print('zipping took: ', time.time() - t1)
#
#     i = 1
#     for movie_id, name_n_year in zipped:
#         print('\n', i)
#         i += 1
#
#         ext_title = name_n_year[0] + ', ' + name_n_year[1]
#
#         print('Getting page content.')
#         t = time.time()
#         page_content = get_page_content(movie_id)
#         print('getting page content took: ', time.time() - t)
#
#         print('Scraping.')
#         t = time.time()
#         movie_to_keyword, keyword_to_movie = scrape_and_get_keywords(
#             ext_title, page_content, movie_to_keyword, keyword_to_movie)
#         print('scraping took: ', time.time() - t)
#
#     return movie_to_keyword, keyword_to_movie
#

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
    t1 = time.time()
    data = Data()
    # print(data.get_extended_names())


    # a_title = 'The Godfather'
    # movie_ids = data.title_to_id(a_title)
    # m_id = movie_ids.pop()
    # print(m_id)
    # page_content = get_page_content(m_id)
    #
    # print('getting done..')
    # movie_to_keyword, keyword_to_movie = scrape_page_content(
    #     a_title, page_content, movie_to_keyword, keyword_to_movie)
    #
    # movie_to_keyword, keyword_to_movie = create_dict_keyword_to_movie(data)
    #
    # print_movie_to_keyword(50, movie_to_keyword)
    # print("----------------------------------")
    # print_keyword_to_movie(50, keyword_to_movie)

    movie_name = "Sungurlar"
    tags_of_movie = search_by_name(data, movie_name)
    print(tags_of_movie)

    t2 = time.time()
    print(t2 - t1)
