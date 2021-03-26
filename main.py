from imdbScraper import *

movie_keyword = {}
keyword_movie = {}

page_content = get_page_content("tt0068646")

movie_keyword, keyword_movie = scrape_page_content("The Godfather", page_content, movie_keyword, keyword_movie)

i = 0
for keyword in movie_keyword:
    print(keyword)
    i += 1
    if i > 50:
        break

for movie in keyword_movie:
    print(movie)
    i += 1
    if i > 100:
        break
