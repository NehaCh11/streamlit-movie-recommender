import streamlit as st
import pickle
import pandas as pd
import requests


# Function to fetch movie poster using TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkY2I4YWRiODIxM2U1YTBkZDljOWUxMWUzMWI5YzEwMCIsIm5iZiI6MTY3MTE5NTgxNi42NzcsInN1YiI6IjYzOWM2Y2E4MTg4NjRiMDA3ZGRkNGRiZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pRL0DCDvvo4_abYZY39YDjO_4K-j7B0EblHtyX8hC0M"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')


# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Streamlit UI
st.title("🎬 Movie Recommender System")
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button("Recommend", key="recommend_button"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
