import pickle
import requests
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

TMDB_API_KEY = "d2883c382e5d98b3a7f33b1c22616369"

TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

FALLBACK_POSTER = "https://placehold.co/500x750?text=Poster+Not+Available"


@st.cache_resource
def load_data():

    try:
        with open("movie_dict.pkl", "rb") as file:
            movies_data = pickle.load(file)

        with open("similarity.pkl", "rb") as file:
            similarity_data = pickle.load(file)

        if isinstance(movies_data, dict):
            movies_data = pd.DataFrame(movies_data)

        return movies_data, similarity_data

    except FileNotFoundError as e:
        st.error(f"File not found: {e.filename}")
        st.stop()

    except Exception as e:
        st.error(f"Error loading files: {e}")
        st.stop()


movies, similarity = load_data()



MOVIE_ID_COLUMN = None

possible_id_columns = [
    "movie_id",
    "id",
    "tmdb_id"
]

for column in possible_id_columns:
    if column in movies.columns:
        MOVIE_ID_COLUMN = column
        break


@st.cache_data(ttl=86400)
def fetch_poster(movie_id):

    if movie_id is None:
        return FALLBACK_POSTER

    try:
        movie_id = int(movie_id)

    except (ValueError, TypeError):
        return FALLBACK_POSTER

    url = f"{TMDB_MOVIE_URL}{movie_id}"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return FALLBACK_POSTER

        if not response.text.strip():
            return FALLBACK_POSTER

        try:
            data = response.json()

        except Exception:
            return FALLBACK_POSTER

        poster_path = data.get("poster_path")

        if not poster_path:
            return FALLBACK_POSTER

        return f"{TMDB_IMAGE_BASE_URL}{poster_path}"

    except requests.exceptions.RequestException:
        return FALLBACK_POSTER


def recommend(movie_title):

    try:
        matched_movies = movies[
            movies["title"] == movie_title
        ]

        if matched_movies.empty:
            return [], []

        movie_index = matched_movies.index[0]

        try:
            movie_position = movies.index.get_loc(movie_index)
        except Exception:
            movie_position = movie_index

        distances = similarity[movie_position]

        movie_list = sorted(
            enumerate(distances),
            key=lambda x: x[1],
            reverse=True
        )

        recommended_names = []
        recommended_posters = []

        seen_titles = set()

        for index, score in movie_list:

            if index == movie_position:
                continue

            if index >= len(movies):
                continue

            movie_row = movies.iloc[index]

            title = movie_row["title"]

            if title in seen_titles:
                continue

            seen_titles.add(title)

            if MOVIE_ID_COLUMN:
                movie_id = movie_row[MOVIE_ID_COLUMN]
            else:
                movie_id = None

            recommended_names.append(title)

            recommended_posters.append(
                fetch_poster(movie_id)
            )

            if len(recommended_names) == 5:
                break

        return recommended_names, recommended_posters

    except Exception as e:
        st.error(f"Recommendation error: {e}")
        return [], []

st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and get the top 5 similar movie recommendations."
)


movie_titles = (
    movies["title"]
    .dropna()
    .astype(str)
    .drop_duplicates()
    .sort_values()
    .tolist()
)


selected_movie = st.selectbox(
    "Select a movie",
    movie_titles
)



if st.button(
    "RECOMMEND",
    type="primary",
    use_container_width=True
):

    with st.spinner("Finding similar movies..."):

        names, posters = recommend(
            selected_movie
        )

    if not names:

        st.warning("No recommendations found.")

    else:

        st.subheader("Recommended Movies")

        columns = st.columns(5)

        for i in range(len(names)):

            with columns[i]:

                st.image(
                    posters[i],
                    use_container_width=True
                )

                st.markdown(
                    f"**{names[i]}**"
                )

with st.expander("Dataset Information"):

    st.write(
        f"Total movies: **{len(movies)}**"
    )

    st.write("Columns:")

    st.write(
        list(movies.columns)
    )

    if MOVIE_ID_COLUMN:

        st.success(
            f"Movie ID column detected: {MOVIE_ID_COLUMN}"
        )

    else:

        st.warning(
            "No movie_id / id / tmdb_id column found."
        )


