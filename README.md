# 🎧 Spotify Mood-Based Music Recommender

A machine learning app that recommends songs based on your mood using K-Means Clustering and a Spotify Top 2010–2019 dataset.

## 💡 Features

- 🎯 Clusters songs into 4 moods: Happy, Chill, Energetic, Sad
- 📊 Uses valence, energy, danceability, and acousticness features
- 🚀 Deployed using Streamlit for an interactive web experience

## 🔍 Dataset

Used the [Top Spotify Songs from 2010–2019](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year) dataset from Kaggle.

## 🛠 Tech Stack

- Python, Pandas, Scikit-learn
- KMeans Clustering
- Streamlit for UI

## 🌐 Live Demo

👉 [Live App](https://yourusername-streamlit-app.streamlit.app)

## 📷 Preview

![App Screenshot](screenshot.png) <!-- optional if you add a screenshot -->

## ⚙️ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/spotify-mood-recommender.git
cd spotify-mood-recommender
pip install -r requirements.txt
streamlit run app.py
