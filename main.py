from imdbScraper import *

movie_keyword = {}
keyword_movie = {}

page_content = get_page_content("tt0068646")

movie_keyword, keyword_movie = scrape_page_content("The Godfather", page_content, movie_keyword, keyword_movie)


print("hello")
