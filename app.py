import pandas as pd
import streamlit as st
import requests
import pickle
import base64
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("movie_img.jpg")

page_bg_img = (f"\n"
               f"<style>\n"
               f"[data-testid=\"stAppViewContainer\"] > .main {{\n"
               f"background-image =(\"movie_img.jpg\");\n"
               f"background-size: 180%;\n"
               f"background-position: top left;\n"
               f"background-repeat: no-repeat;\n"
               f"background-attachment: local;\n"
               f"}}\n"
               f"\n"
               f"[data-testid=\"stSidebar\"] > div:first-child {{\n"
               f"background-image: url(\"data:image/png;base64,{img}\");\n"
               f"background-position: center; \n"
               f"background-repeat: no-repeat;\n"
               f"background-attachment: fixed;\n"
               f"}}\n"
               f"\n"
               f"[data-testid=\"stHeader\"] {{\n"
               f"background: rgba(0,0,0,0);\n"
               f"}}\n"
               f"\n"
               f"[data-testid=\"stToolbar\"] {{\n"
               f"right: 2rem;\n"
               f"}}\n"
               f"</style>\n")

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.header("Configuration")


def fetch_poster(movie_id):
    responce = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
            .format(movie_id))
    data = responce.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = simi[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies_10 = []
    recommend_movies_poster = []
    movie_genres = []
    cast_movies = []
    movie_Director = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies_10.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
        genre = (movies_for_cast.iloc[i[0]].genres)
        ge = '\n'.join(genre)
        movie_genres.append(ge)
        cast = (movies_for_cast.iloc[i[0]].cast)
        text = '\n'.join(cast)
        cast_movies.append(text)
        direc = (movies_for_cast.iloc[i[0]].crew)
        di = '\n'.join(direc)
        movie_Director.append(di)

    return recommend_movies_10, recommend_movies_poster, movie_genres, cast_movies, movie_Director


simi = pickle.load(open('simi.pkl', 'rb'))
st.title('MOVIE RECOMMENDER SYSTEM')

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie_for = pickle.load(open('movie_for_all_info.pkl', 'rb'))
movies_for_cast = pd.DataFrame(movie_for)
movies = pd.DataFrame(movie_dict)
selected_movie_name = st.selectbox(
    'Please Enter The Movie Name',
    movies['title'].values)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters, movie_genres, cast_movies, movie_Director = recommend(
        selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.subheader(':red[Movie]')
        st.text(recommended_movie_names[0])
        st.subheader(':red[Genres]')
        st.text(movie_genres[0])
        st.subheader(':red[Top 3 Cast]')
        st.text(cast_movies[0])
        st.subheader(':red[Director]')
        st.text(movie_Director[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.subheader(':red[Movie]')
        st.text(recommended_movie_names[1])
        st.subheader(':red[Genres]')
        st.text(movie_genres[1])
        st.subheader(':red[Top 3 Cast]')
        st.text(cast_movies[1])
        st.subheader(':red[Director]')
        st.text(movie_Director[1])

    with col3:
        st.image(recommended_movie_posters[2])
        st.subheader(':red[Movie]')
        st.text(recommended_movie_names[2])
        st.subheader(':red[Genres]')
        st.text(movie_genres[2])
        st.subheader(':red[Top 3 Cast]')
        st.text(cast_movies[2])
        st.subheader(':red[Director]')
        st.text(movie_Director[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.subheader(':red[Movie]')
        st.text(recommended_movie_names[3])
        st.subheader(':red[Genres]')
        st.text(movie_genres[3])
        st.subheader(':red[Top 3 Cast]')
        st.text(cast_movies[3])
        st.subheader(':red[Director]')
        st.text(movie_Director[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.subheader(':red[Movie]')
        st.text(recommended_movie_names[4])
        st.subheader(':red[Genres]')
        st.text(movie_genres[4])
        st.subheader(':red[Top 3 Cast]')
        st.text(cast_movies[4])
        st.subheader(':red[Director]')
        st.text(movie_Director[4])
