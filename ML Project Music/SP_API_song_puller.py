import os
from dotenv import load_dotenv  # Import load_dotenv to read .env file
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

#load environment variables from .env file
load_dotenv()

#Spotify API Credentials.. (need to hide?)
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

#Authenticate with Sptoify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

#function to retreive songs
def get_songs_by_mood(mood, limit=20):
    """Fetches songs from Spotify based on some mood-related keywords"""
    results = sp.search(q=f'{mood} songs', type="track", limit=limit)
    song_list = []
    for track in results["tracks"]["items"]:
        song_name = track["name"]
        artist = track["artists"][0]["name"]
        song_list.append({"Song_Name": song_name, "Artist": artist, "Sentiment_Label":mood})
    return song_list

#Fetch different songs for each mood and store in a DataFrame
moods = ["Happy", "Sad", "Relaxed", "Motivated"]
all_songs = []
for mood in moods:
    songs = get_songs_by_mood(mood, limit=50)
    all_songs.extend(songs)

df = pd.DataFrame(all_songs)

df.to_csv("music_data.csv", index=False)
print(f"Data saved with {len(df)} songs")