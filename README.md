# 📊 YouTube Trend Analyzer

A keyword-driven YouTube video analysis tool built with Streamlit and the YouTube Data API. This web application helps you explore current video trends by visualizing patterns in titles, upload dates, and popular channels.

Ideal for content creators, researchers, and data enthusiasts looking to extract insights from YouTube metadata.

---

## 🎯 Project Goals

- Discover trending topics in a domain (e.g., AI, health, education)
- Visualize how content around a keyword is distributed
- Understand which channels dominate certain niches
- Make sense of unstructured title data using WordClouds

---

## 🖼️ App Demo

> Screenshot 2025-06-11 120035.png
> Figure_1.png ( Common words in trending titles plot)

---

## 🔍 Key Features

| Feature                      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 🔎 Keyword Search            | Enter a topic to search YouTube videos (e.g., "AI", "Mental Health", "UPSC")|
| 📋 Metadata Table            | See a table of top videos with title, channel name, and publish date        |
| ☁️ WordCloud                 | Highlights most frequent terms in video titles                              |
| 📊 Channel Frequency Chart   | Shows which channels have the most videos on the topic                      |
| 📅 Publish Date Chart        | Displays number of videos by upload date                                    |
| 🔄 Interactive UI            | Streamlit-powered user interface                                            |

---

## 🛠 Built With

- **Frontend / UI**: [Streamlit](https://streamlit.io)
- **API**: [YouTube Data API v3](https://developers.google.com/youtube/v3)
- **Data Processing**: `pandas`
- **Visualizations**: `matplotlib`, `seaborn`, `wordcloud`
- **Environment**: Python 3.8+

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8 or above
- Google account to generate YouTube API key (free)

### 🔐 Get a YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **YouTube Data API v3**
3. Go to **APIs & Services > Credentials**
4. Create an API key → Copy it for use in the app

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mariam-biju/youtube_video_analyzer.git
cd youtube_video_analyzer
