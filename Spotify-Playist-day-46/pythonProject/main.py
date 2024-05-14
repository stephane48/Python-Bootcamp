from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

SPOTIPY_CLIENT_ID = "xxxx"
SPOTIPY_CLIENT_SECRET = "xxxx"
SPOTIPY_REDIRECT_URI = "http://example.com"
# SPOTIFY_USERNAME = "xxxx"

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
top_songs = response.text
soup = BeautifulSoup(top_songs, "html.parser")
songs = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in songs]
# print(song_titles)

# Spotify Authentication
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope, cache_path=".cache-f51erjznw2r323hlx1d3al249",
        )
    )
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uri = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")
print(song_uri)

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
