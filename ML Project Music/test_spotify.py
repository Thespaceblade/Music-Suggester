import os
from dotenv import load_dotenv
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-library-read user-read-private"
))

# Run the API call with only seed_genres and limit
results = sp.recommendations(seed_genres=["pop"], limit=50)
print(results)