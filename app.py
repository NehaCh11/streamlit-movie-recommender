import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data with tags
movies = pickle.load(open('movies.pkl', 'rb'))

# Build similarity matrix dynamically
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# Function to fetch poster using TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkY2I4YWRiODIxM2U1YTBkZDljOWUxMWUzMWI5YzEwMCIsIm5iZiI6MTY3MTE5NTgxNi42NzcsInN1YiI6IjYzOWM2Y2E4MTg4NjRiMDA3ZGRkNGRiZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pRL0DCDvvo4_abYZY39YDjO_4K-j7B0EblHtyX8hC0M"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"

# Recommend movies function
def recommend(movie):
    movie = movie.lower()
    matches = movies[movies['title'].str.lower() == movie]
    if matches.empty:
        return [], []

    index = matches.index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters

# Streamlit interface
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Pick a movie to get recommendations:", movies['title'].values)

if st.button("Recommend", key="recommend_button"):
    names, posters = recommend(selected_movie)

    if names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])
    else:
        st.warning("Movie not found in the dataset.")
