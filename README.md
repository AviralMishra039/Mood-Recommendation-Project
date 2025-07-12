# 🎧 Spotify Mood-Based Music Recommender

A machine learning project that recommends Spotify songs based on your mood using unsupervised learning and audio features from the top 10 Spotify songs from 2010–2019. Built with Python, Streamlit, and KMeans clustering.

![App Preview](/images/app_screenshot.png)

[Check out the app](https://mood-recommendation-project-czkdt6drmxwdjmibfjvaru.streamlit.app/)

---

## 📌 Features

- 🎵 Clustered songs based on mood (Happy, Chill, Sad, Energetic)
- 🤖 KMeans clustering on features like energy, valence, danceability, and acousticness
- ⚡ Instant recommendations based on your selected mood
- 🌐 Deployed as an interactive Streamlit web app

---

## 📂 Dataset

- **Source**: [Top Spotify Songs 2010–2019](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year)
- **Columns used**: `val` (valence), `nrgy` (energy), `dnce` (danceability), `acous` (acousticness)

---

## ⚙️ Tech Stack

- **Python** 🐍
- **Streamlit** – for building the web interface
- **Pandas & NumPy** – for data manipulation
- **Matplotlib & Seaborn** – for visualization
- **Scikit-Learn** – for clustering with KMeans

---

## 🧠 How It Works

1. The dataset is cleaned and relevant features (`val`, `nrgy`, `dnce`, `acous`) are selected.
2. KMeans clustering groups songs into 4 clusters, representing different moods.
3. These clusters are manually labeled based on average feature values.
4. The user selects a mood, and songs from that cluster are recommended.

---

### Feel free to check out my other projects on [LinkedIn](https://www.linkedin.com/in/aviral-mishra-138237338/)
