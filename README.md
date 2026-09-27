# 🎬 Movie Recommendation System

<p align="center">
  <b>An end-to-end Machine Learning web application for discovering similar movies using content-based filtering and cosine similarity.</b>
</p>

<p align="center">
  Built with Python, Scikit-learn, Streamlit, Pandas, NumPy, and TMDB API.
</p>

<p align="center">
  <a href="https://movie-recommendation-system-ejeudiuexncv3zsmpsaaaj.streamlit.app/">
    🚀 Live Demo
  </a>
</p>

---

## 🖥️ Application Preview

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/2331dbef-791b-413a-899c-3d3885b8222f"
    alt="Movie Recommendation System Preview"
    width="100%"
  >
</p>

<p align="center">
  <i>Select a movie and get the top 5 most similar movie recommendations with posters.</i>
</p>

## 📌 Project Overview

The **Movie Recommendation System** is an end-to-end Machine Learning project that recommends movies similar to a selected movie.

The system uses a **content-based filtering approach** and **cosine similarity** to compare movies based on their metadata and identify the most relevant recommendations.

Movie posters are fetched dynamically using the **TMDB API**, while the complete application is built and deployed using **Streamlit**.

This project demonstrates practical skills in:

- Machine Learning
- Recommendation Systems
- Data Preprocessing
- Feature Engineering
- Similarity Modeling
- API Integration
- Streamlit Development
- Cloud Deployment

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Build a content-based movie recommendation engine.
2. Analyze similarity between movies.
3. Apply cosine similarity for recommendation ranking.
4. Preprocess movie metadata for machine learning.
5. Generate the top 5 most similar movies.
6. Integrate the TMDB API for movie posters.
7. Build an interactive Streamlit interface.
8. Deploy the application using Streamlit Community Cloud.

---

## ✨ Features

- 🎬 Interactive movie selection
- 🤖 Machine Learning-based recommendations
- 🔍 Top 5 similar movie suggestions
- 🖼️ Movie posters using TMDB API
- ⚡ Fast recommendations using a precomputed similarity matrix
- 🎨 Clean Streamlit user interface
- ☁️ Live deployment on Streamlit Community Cloud
- 🛡️ Error handling for missing posters and API failures

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Recommendation System**.

The recommendation engine analyzes movie metadata and compares movies based on their content.

The process includes:

- Data cleaning
- Feature selection
- Feature engineering
- Text processing
- Vectorization
- Cosine similarity
- Recommendation ranking

Movies with higher similarity scores are considered more closely related.

---

## 🔄 Project Workflow

```text
              Movie Dataset
                    │
                    ▼
             Data Preprocessing
                    │
                    ▼
            Feature Engineering
                    │
                    ▼
            Text Vectorization
                    │
                    ▼
            Cosine Similarity
                    │
                    ▼
           Similarity Matrix
                    │
                    ▼
         User Selects a Movie
                    │
                    ▼
       Top 5 Similar Movies
                    │
                    ▼
            TMDB API Request
                    │
                    ▼
          Movie Poster Display
                    │
                    ▼
       Streamlit Web Application
