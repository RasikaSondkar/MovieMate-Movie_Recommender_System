import streamlit as st
import pickle
import pandas as pd
import requests

api_key=st.secrets["TMDB_API_KEY"]


def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id


        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster((movie_id)))
    return recommended_movies,recommended_movies_posters


movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pkl","rb"))





st.title("🎬 MovieMate")
st.caption("Discover movies you'll love, powered by AI.")



st.markdown("""
<style>
/* Main background */
.stApp {
    background: #F5F6F8;
    color: #263238;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Headings and text */
h1, h2, h3, p, label {
    color: #263238;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 42px 20px 30px;
    background: #FFFFFF;
    border: 1px solid #E2E6EA;
    border-radius: 18px;
    margin-bottom: 28px;
}

.hero-tag {
    color: #526B82;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
}

.hero h1 {
    color: #263238;
    font-size: clamp(34px, 5vw, 52px);
    font-weight: 800;
    margin: 15px 0;
}

.hero h1 span {
    color: #526B82;
}

.hero p {
    color: #65727D;
    font-size: 17px;
}

/* Movie selector */
[data-testid="stSelectbox"] > label {
    color: #263238;
    font-weight: 700;
}

[data-testid="stSelectbox"] > div > div {
    background: #FFFFFF;
    border: 1px solid #D7DEE5;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background: #526B82;
    color: #FFFFFF;
    border: 1px solid #526B82;
    border-radius: 10px;
    min-height: 44px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #40566B;
    color: #FFFFFF;
    border-color: #40566B;
}

/* Movie posters */
[data-testid="stImage"] img {
    border-radius: 10px;
    transition: transform 0.2s ease;
}

[data-testid="stImage"] img:hover {
    transform: scale(1.02);
}

/* Divider */
hr {
    border-color: #E0E5EA;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-tag">YOUR PERSONAL CINEMA</div>
    <h1>Find your next <span>favorite movie.</span></h1>
    <p>Less scrolling. More watching. Discover films picked just for you.</p>
</div>
""", unsafe_allow_html=True)




selected_movies_name =st.selectbox("How would you like to be connected?",
                     movies['title'].values)


if st.button("Recommend"):
    names,posters=recommend(selected_movies_name)


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

