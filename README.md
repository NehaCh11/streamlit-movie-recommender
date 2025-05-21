# streamlit-movie-recommender

🎬 Movie Recommender System

This is a content-based movie recommender system built using Python, scikit-learn, and Streamlit. It recommends movies based on metadata such as genre, keywords, cast, crew, and overview, and displays movie posters using the TMDb API.

🚀 Live Demo
👉 Try it live:
https://app-movie-recommender-emgwhrafywnryrd4qz4emm.streamlit.app/

🧠 How It Works
Loads preprocessed movie metadata (movies.pkl)

Combines overview, genres, keywords, cast, and crew into a single "tags" field

Converts tags into vectors using CountVectorizer

Computes similarity using cosine similarity

Recommends top 5 similar movies with posters via TMDb API

📁 Project Structure
movie-recommender-system/
├── app.py → Main Streamlit app file
├── movies.pkl → Processed movie data
├── requirements.txt → Python dependencies
├── .gitignore → Git ignored files
└── README.md → This file

💻 Run Locally
Clone the repo
git clone https://github.com/your-username/streamlit-movie-recommender.git
cd streamlit-movie-recommender

Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app.py

📦 Requirements
streamlit

pandas

numpy

scikit-learn

nltk

requests

📌 License
This project is licensed under the MIT License.

🙋‍♀️ Author
Built with ❤️ by @NehaCh11
Live app 👉 https://app-movie-recommender-emgwhrafywnryrd4qz4emm.streamlit.app/
