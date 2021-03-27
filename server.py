import eel
import time

eel.init('web')


@eel.expose
def search(movieName, keywordName, contentType, year):
    print(movieName, keywordName, contentType, year)


eel.start('main.html', mode="chrome-app", host="localhost", port=8080)
