import requests
import random
from bs4 import BeautifulSoup

movies = []
genres = ["Comedy", "Drama", "Romance", "Action", "Adventure", "Crime", "Family", "Musical", "Horror",
          "Fantasy", "Thriller", "Sci-Fi", "Music", "Mystery", "Documentary", "Animation", "Sport",
          "Western", "Biography", "War", "History", "News", "Reality-TV", "Talk-Show", "Film-Noir",
          "Game-Show", "Short", ""]


def getmovie(genre):
    isgenre = False
    for choice in genres:
        if genre == choice:
            isgenre = True

    if not isgenre:
        print("You have selected an invalid genre. Please pick from the following genres and try again!")
        getgenres()
        return "You have selected an invalid genre. Please pick a valid genre!"

    urlstring = "https://www.imdb.com/search/title/?title_type=movie&genres=" + genre + \
                "&sort=num_votes,desc&explore=title_type,genres"

    page = requests.get(urlstring)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("h3", class_="lister-item-header")

    for result in results:
        title = result.find('a')
        movies.append(title.text)

    r =random.randint(0, len(movies))

    print(movies[r])
    return movies[r]


def getgenres():
    for genre in genres:
        print(genre)

