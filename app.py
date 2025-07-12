import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import random

# Title
st.title("🎧 Spotify Mood-Based Music Recommender")

# Loading data
df = pd.read_csv("top10s.csv", encoding='latin1')

# Dropping unnecessary columns
df.drop(columns=['Unnamed: 0', 'title', 'artist', 'top genre', 'year'], inplace=False)

# Preprocessing
features = df[['val', 'nrgy', 'dnce', 'acous']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

#  Applying KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
df['mood_cluster'] = kmeans.fit_predict(scaled_features)

# Label moods
mood_labels = {
    0: "Rock / Energetic",
    1: "Sad",
    2: "Happy / Dance",
    3: "Chill Vibes"
}
df['mood'] = df['mood_cluster'].map(mood_labels)

# Mood selection
selected_mood = st.selectbox("Choose your mood", df['mood'].unique())

# Recommend button
if st.button("🎵 Recommend Songs"):
    recommendations = df[df['mood'] == selected_mood].sample(5)
    st.write("Here are some songs for your mood:")
    st.dataframe(recommendations[['title', 'artist', 'year', 'top genre']])
