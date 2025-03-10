import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# Load the dataset
file_path = 'ML.csv'  # Ensure the CSV file is in the same directory as the script
df = pd.read_csv(file_path)

# Function to categorize songs based on valence and energy
def categorize_sentiment(row):
    if row['valence'] > 0.6 and row['energy'] > 0.5:
        return 'Happy'
    elif row['valence'] < 0.3 and row['energy'] < 0.4:
        return 'Sad'
    elif row['valence'] > 0.5 and row['energy'] < 0.5:
        return 'Relaxed'
    elif row['valence'] < 0.5 and row['energy'] > 0.6:
        return 'Motivated'
    else:
        return 'Neutral'

# Apply sentiment classification
df['Sentiment_Label'] = df.apply(categorize_sentiment, axis=1)

# Function to detect sentiment based on user input
def get_sentiment(user_input: str) -> str:
    """Determines the sentiment category based on user input."""
    user_input = user_input.lower()
    if any(word in user_input for word in ['happy', 'joy', 'excited', 'glad', 'fun']):
        return 'Happy'
    elif any(word in user_input for word in ["sad", "upset", "depressed", "cry", "heartbroken"]):
        return 'Sad'
    elif any(word in user_input for word in ["relax", "calm", "chill", "peaceful", "serene"]):
        return "Relaxed"
    elif any(word in user_input for word in ["motivate", "strong", "energy", "power", "inspire"]):
        return "Motivated"
    else:
        return "Neutral"  # Default if no keyword matches

# Function to recommend a song based on user input
def recommend_song():
    user_input = entry.get() 
    sentiment = get_sentiment(user_input) 

    if sentiment == 'Neutral':
        messagebox.showinfo("Recommendation", "I'm sorry, I couldn't understand your sentiment. Try expressing an emotion!") 
        return

    # Filter songs based on detected sentiment
    filtered_songs = df[df['Sentiment_Label'] == sentiment]

    if filtered_songs.empty:
        messagebox.showinfo("Recommendation", "I'm sorry, I couldn't find any songs for your sentiment.")
    else:
        song = filtered_songs.sample(n=1).iloc[0]     
        messagebox.showinfo("Recommendation", 
                            f"Based on your sentiment, I recommend '{song['track_name']}' by {song['artists']}.\n")
                            

# GUI Setup
root = tk.Tk()
root.title("Music Recommendation System")
root.geometry("500x250")

# Label
label = tk.Label(root, text="How are you feeling today?", font=('Arial', 12))
label.pack(pady=10)

# Text Entry Box
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Recommend Button
recommend_button = tk.Button(root, text="Recommend Song", command=recommend_song, font=('Arial', 12))
recommend_button.pack(pady=20)

root.mainloop()