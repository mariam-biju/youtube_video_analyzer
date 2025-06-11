from googleapiclient.discovery import build
import pandas as pd

api_key = "<YOUR_API_KEY>"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_videos(query, max_results=50):
    videos = []
    request = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type='video'
    )
    response = request.execute()
    for item in response['items']:
        video = {
            'video_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'published': item['snippet']['publishedAt']
        }
        videos.append(video)
    return pd.DataFrame(videos)

df = get_videos("artificial intelligence")
print(df.head())

#**********************************************************************

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(df['title'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Trending Titles")
plt.show()

#**********************************************************************

df['published'] = pd.to_datetime(df['published'])
df['date'] = df['published'].dt.date

df['date'].value_counts().sort_index().plot(kind='bar', figsize=(10,5), title="Upload Count by Date")
plt.tight_layout()
plt.show()

#**********************************************************************

import streamlit as st

st.title("YouTube Trend Analyzer")
st.write("Explore trending videos for a keyword")

query = st.text_input("Enter search keyword")

if query:
    df = get_videos(query)
    st.write(df.head())


