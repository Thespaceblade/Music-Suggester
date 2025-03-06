# Music Suggester

📌 Project Overview

Music Suggester is a sentiment-based music recommendation system that suggests songs based on a user’s mood. It analyzes text input, detects the emotional tone, and fetches relevant songs from a dataset or Spotify’s API.

🚀 Features

Sentiment Analysis: Detects emotions from user input (Happy, Sad, Relaxed, Motivated).
Song Recommendation: Matches moods with appropriate songs.
Spotify API Integration: Dynamically fetches songs from Spotify.
Graphical User Interface (GUI): Uses Tkinter for an interactive experience.
🛠️ Installation & Setup

1️⃣ Clone the Repository
 git clone https://github.com/Thespaceblade/Music-Suggester.git
 cd Music-Suggester
2️⃣ Set Up a Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate    # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up Spotify API Credentials
Create a .env file in the root folder and add:

SPOTIPY_CLIENT_ID='your_client_id'
SPOTIPY_CLIENT_SECRET='your_client_secret'
⚠️ Never expose your API credentials in public repositories! Use .gitignore to exclude the .env file.
5️⃣ Run the Application
python Music_Suggester.py
🎨 How It Works

User Input: Enter a phrase describing your mood.
Sentiment Analysis: The script classifies the mood.
Song Matching:
If a local dataset is used, it finds a song that matches the sentiment.
If Spotify API is enabled, it fetches new songs dynamically.
Recommendation: The selected song is displayed.
🏗️ Project Structure

Music-Suggester/
│── .venv/                   # Virtual environment (optional)
│── .gitignore               # Ignore sensitive files
│── requirements.txt         # Dependencies
│── Music_Suggester.py       # Main script
│── SP_API_song_puller.py    # Spotify API integration
│── music_data.csv           # Local dataset (if used)
│── README.md                # This file
🛠️ Tech Stack

Python 🐍
Spotipy (Spotify API) 🎵
Tkinter (GUI) 🖥️
pandas (Data Handling) 📊
dotenv (Environment Variables) 🔐
🚀 Contributing

Fork the repo.
Create a new branch (feature-branch):
git checkout -b feature-branch
Commit changes:
git commit -m "Added new feature"
Push to GitHub:
git push origin feature-branch
Open a Pull Request.
📜 License

This project is licensed under the MIT License. Feel free to modify and improve it!

🎶 Happy Coding & Keep Jamming! 🎧

