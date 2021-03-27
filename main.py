from imdbScraper import *
from pull_id_from_tsv import *

movie_keyword = {}
keyword_movie = {}

data = Data()
movie_id = data.title_to_id('The Godfather')

page_content = get_page_content(movie_id)

movie_keyword, keyword_movie = scrape_page_content("The Godfather", page_content, movie_keyword, keyword_movie)

i = 0
for movie in movie_keyword:
    print(movie)
    i += 1
    if i > 50:
        break
print("----------------------------------")
for keyword in keyword_movie:
    print(keyword)
    i += 1
    if i > 100:
        break
