from bs4 import BeautifulSoup
import requests
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
greatest_movies = response.text

soup = BeautifulSoup(greatest_movies, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_name = [movie.getText() for movie in movies]
movies_names = movie_name[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_names:
        file.write(f"{movie}\n")
