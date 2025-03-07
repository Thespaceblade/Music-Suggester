import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# Load the dataset
file_path = 'music_data.csv'
df = pd.read_csv(file_path)

# Function to detect sentiment based on user input
def get_sentiment(user_input: str) -> str:
    """This function takes a user input and returns the corresponding sentiment."""
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
    user_input = entry.get() #Get input from GUI bo
    sentiment = get_sentiment(user_input) #Pulling from other function to get sentiment
    """This function recommends a song based on the user's input sentiment."""
    if sentiment == 'Neutral':
        messagebox.showinfo("Recommendation", "I'm sorry, I couldn't understand your sentiment, try expressing an emotion!") 
        return
    #Filter songs based on detected sentiment
    filtered_songs = df[df['Sentiment_Label'] == sentiment]
    if filtered_songs.empty:
        messagebox.showinfo("Recommendation", "I'm Sorry, I couldn't find any songs for your sentiment")
    else:
        song = filtered_songs.sample(n=1, random_state=None).iloc[0]     # Randomly select a song from the filtered songs
        messagebox.showinfo("Recommendation", f"Based on your sentiment, I would recommend the song '{song['Song_Name']}' by {song['Artist']}")
    
#GUI Setup
root = tk.Tk()
root.title("Music Recommendation System")
root.geometry("400x200")

#Label
label = tk.Label(root, text="How are you feeling today?", font=('Arial', 12))
label.pack(pady=10)

#Text Extry Box
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

#Recomend Button
recommend_button = tk.Button(root, text="Recommend Song", command=recommend_song, font=('Arial', 12))
recommend_button.pack(pady=20)
                      
root.mainloop()

