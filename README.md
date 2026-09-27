# 🎬 Movie Recommendation System

<p align="center">
  <b>An end-to-end Machine Learning web application that recommends similar movies using content-based filtering and cosine similarity.</b>
</p>

<p align="center">
  Built with Python, Scikit-learn, Streamlit and TMDB API.
</p>

<p align="center">
  <a href="https://movie-recommendation-system-ejeudiuexncv3zsmpsaaaj.streamlit.app/">
    🚀 Live Demo
  </a>
  &nbsp; • &nbsp;
  <a href="#-how-it-works">🧠 How It Works</a>
  &nbsp; • &nbsp;
  <a href="#-tech-stack">🛠 Tech Stack</a>
</p>

---

## 🖥️ Application Preview

<p align="center">
  <img src="assets/app-preview.png" alt="Movie Recommendation System Preview" width="100%">
</p>

<p align="center">
  <i>Select a movie and instantly discover the top 5 most similar movies with posters.</i>
</p>

---

## 🚀 Live Demo

The application is deployed on **Streamlit Community Cloud**.

### 👉 [Open Movie Recommendation System](https://movie-recommendation-system-ejeudiuexncv3zsmpsaaaj.streamlit.app/)

---

## 📌 About the Project

The **Movie Recommendation System** is a Machine Learning project designed to help users discover movies similar to their interests.

The application uses a **content-based recommendation approach** to analyze movie similarity and return the **top 5 most relevant recommendations**.

Movie posters are fetched dynamically using the **TMDB API**, while the user interface is built and deployed using **Streamlit**.

This project demonstrates an end-to-end workflow involving:

- Data preprocessing
- Feature extraction
- Machine Learning
- Similarity computation
- API integration
- Web application development
- Cloud deployment

---

## ✨ Features

- 🎬 Select a movie from the available movie database
- 🤖 Generate ML-based movie recommendations
- 🔍 Find the top 5 most similar movies
- 🖼️ Display movie posters using the TMDB API
- ⚡ Fast recommendations using a precomputed similarity matrix
- 🎨 Clean and interactive Streamlit interface
- ☁️ Deployed using Streamlit Community Cloud
- 🛡️ Handles missing posters and API errors

---

## 🧠 How It Works

The recommendation engine follows a **Content-Based Filtering** approach.

```text
Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Text / Metadata Vectorization
     ↓
Cosine Similarity
     ↓
Similarity Matrix
     ↓
User Selects a Movie
     ↓
Top 5 Similar Movies
     ↓
TMDB Poster API
     ↓
Streamlit Web Application
