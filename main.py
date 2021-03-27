from imdbScraper import *

movie_keyword = {}
keyword_movie = {}

page_content = get_page_content("tt0068646")

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
