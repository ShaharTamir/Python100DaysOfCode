from bs4 import BeautifulSoup
import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyOAuth
import requests
from os import environ

SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = environ.get("SPOTIPY_CLIENT_SECRET")


def parse_song_title(song):
    song_text = song.findNext(id="title-of-a-story", class_="a-font-primary-bold-s").text
    song_title = " ".join(song_text.split())
    return song_title


def parse_artist_name(song):
    splitters = ["Featuring", "Feat.", "&", "/"]
    artist_text = song.findNext(name="span", class_="a-font-primary-s").text
    artist_name = " ".join(artist_text.split())
    for sign in splitters:
        if sign in artist_name:
            artist_name = " ".join(artist_name.split(sign)[0].split())

    return artist_name


def find_track_from_spotify(possibilities: list, title, artist_name):
    for track in possibilities:
        for artist in track["artists"]:
            if (artist_name in artist["name"] or "the " + artist_name in artist_name) and \
               title in track["name"]:
                return track

    return possibilities[0]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs_data = soup.find_all(class_="o-chart-results-list-row-container")
songs_titles = [parse_song_title(song) for song in songs_data]
songs_artists = [parse_artist_name(song) for song in songs_data]

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri= "http://example.com",
        scope="playlist-modify-private"
    )
)

user_id = spotify.current_user()["id"]

track_ids = []
for i in range(0, len(songs_titles)):
    results = spotify.search(q=f"track: {songs_titles[i]} artist: {songs_artists[i]}", type="track")
    try:
        track = find_track_from_spotify(results["tracks"]["items"], songs_titles[i], songs_artists[i])
        track_ids.append(track["id"])
    except (SpotifyException, IndexError):
        print(f"track {songs_titles[i]} by {songs_artists[i]} is not found!")

playlist = spotify.user_playlist_create(user=user_id, name=f"{date} greatest hits", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=track_ids)
print("playlist created.")
