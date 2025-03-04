import pandas as pd

file_path = '/Users/jasoncharwin/Personal Academic/Personal Code Projects/ML Project Music/music_data.csv'
df = pd.read_csv(file_path)

print(df.head())
print(df["Sentiment"].value_counts())