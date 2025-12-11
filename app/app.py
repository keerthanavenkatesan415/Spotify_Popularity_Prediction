import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
import joblib

# PATHS

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
DB_PATH = BASE_DIR / "data" / "spotify.db"

# LOAD ARTIFACTS (MODEL + SCALERS + FEATURE ORDER)

rf_model = joblib.load(MODEL_DIR / "final_random_forest.pkl")
scaler_numeric = joblib.load(MODEL_DIR / "scaler_numeric.pkl")
scaler_cluster = joblib.load(MODEL_DIR / "scaler_cluster.pkl")
kmeans = joblib.load(MODEL_DIR / "kmeans.pkl")

feature_cols = [line.strip() for line in open(MODEL_DIR / "feature_columns.txt")]

# Columns used during preprocessing
numeric_cols = [
    "year", "danceability", "energy", "key", "loudness", "mode",
    "speechiness", "acousticness", "instrumentalness", "liveness",
    "valence", "tempo", "duration_ms", "time_signature"
]

cluster_features = [
    "danceability", "energy", "key", "loudness", "mode",
    "speechiness", "acousticness", "instrumentalness",
    "liveness", "valence", "tempo", "duration_ms"
]

# DATABASE CONNECTION 

def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# Load distinct genres for dropdown
with get_conn() as conn:
    genres_from_sql = sorted(pd.read_sql("SELECT DISTINCT genre FROM tracks;", conn)["genre"])


# HELPER — Compute Cluster ID for a new song

def compute_cluster_id(song_features: dict):
    """Compute cluster membership using the clustering scaler + KMeans."""
    cluster_input = np.array([[song_features[f] for f in cluster_features]])
    cluster_scaled = scaler_cluster.transform(cluster_input)
    return int(kmeans.predict(cluster_scaled)[0])


# HELPER — Build model input row with correct feature ordering

def build_model_input(song_features: dict, cluster_id: int):
    """Build a DataFrame aligned to the model's expected feature order."""

    # Copy for safety
    song_features = song_features.copy()
    song_features["cluster_id"] = cluster_id   # <-- ALWAYS add

    # Scale numeric columns
    numeric_vals = scaler_numeric.transform([[song_features[c] for c in numeric_cols]])[0]

    # Initialize final row with 0s for ALL model features
    final = {col: 0 for col in feature_cols}

    # Insert scaled numeric values
    for i, col in enumerate(numeric_cols):
        final[col] = numeric_vals[i]

    # Insert categorical + cluster_id
    for key, value in song_features.items():
        if key in final:
            final[key] = value

    # RETURN DataFrame in EXACT correct order
    return pd.DataFrame([final], columns=feature_cols)



# STREAMLIT UI

st.set_page_config(page_title="Spotify Popularity Predictor", layout="wide")
st.title("🎵 Spotify Popularity Prediction & Song Explorer")
# use emojis to make the UI not boring for users to look at until UI can be improved later
tabs = st.tabs(["🔮 Predict Popularity", "🎧 Genre Explorer"])


# TAB 1 — POPULARITY PREDICTION

with tabs[0]:
    st.header("Predict Song Popularity")
    st.write("Enter song characteristics below. Values must reflect actual audio feature scales (0–1 for most).")

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year Released", 1900, 2025, 2020)
        danceability = st.slider("Danceability (0-1)", 0.0, 1.0, 0.5)
        energy = st.slider("Energy (0-1)", 0.0, 1.0, 0.5)
        loudness = st.number_input("Loudness (dB)", -60.0, 0.0, -10.0)
        speechiness = st.slider("Speechiness (0-1)", 0.0, 1.0, 0.05)
        acousticness = st.slider("Acousticness (0-1)", 0.0, 1.0, 0.2)
        instrumentalness = st.slider("Instrumentalness (0-1)", 0.0, 1.0, 0.0)
        genre = st.selectbox("Genre", genres_from_sql)

    with col2:
        liveness = st.slider("Liveness (0-1)", 0.0, 1.0, 0.2)
        valence = st.slider("Valence (0-1)", 0.0, 1.0, 0.5)
        tempo = st.number_input("Tempo (BPM)", 40.0, 250.0, 120.0)
        duration_ms = st.number_input("Duration (ms)", 10000, 500000, 180000)
        key_val = st.number_input("Musical Key (0-11)", 0, 11, 5)
        mode_val = st.number_input("Mode (0=Minor, 1=Major)", 0, 1, 1)
        time_sig = st.number_input("Time Signature (1-7)", 1, 7, 4)

    if st.button("Predict Popularity", type="primary"):
        user_song = {
            "year": year,
            "danceability": danceability,
            "energy": energy,
            "key": key_val,
            "loudness": loudness,
            "mode": mode_val,
            "speechiness": speechiness,
            "acousticness": acousticness,
            "instrumentalness": instrumentalness,
            "liveness": liveness,
            "valence": valence,
            "tempo": tempo,
            "duration_ms": duration_ms,
            "time_signature": time_sig,
            f"genre_{genre}": 1
        }

        # Compute cluster
        cluster_id = compute_cluster_id(user_song)

        # Build input frame for model
        model_input = build_model_input(user_song, cluster_id)

        # Predict
        pred = rf_model.predict(model_input)[0]

        st.success(f"🎯 Predicted Popularity: **{pred:.1f} / 100**")
        st.info(f"Cluster Assigned: **{cluster_id}**")


# TAB 2 — GENRE EXPLORER

with tabs[1]:
    st.header("Explore Songs by Genre")

    with get_conn() as conn:
        genres = sorted(pd.read_sql("SELECT DISTINCT genre FROM tracks;", conn)["genre"])

    selected_genre = st.selectbox("Choose Genre", genres)
    n_results = st.slider("How many songs to show?", 5, 50, 10)

    if st.button("Show Songs"):
        query = """
        SELECT track_name, artist_name, popularity
        FROM tracks
        WHERE genre = ?
        ORDER BY popularity DESC
        LIMIT ?;
        """
        with get_conn() as conn:
            df_g = pd.read_sql(query, conn, params=[selected_genre, n_results])

        st.subheader(f"Top {n_results} Songs in {selected_genre}")
        st.dataframe(df_g, height=400)
