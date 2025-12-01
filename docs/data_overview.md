# Data Overview

## 1. Dataset Description
This dataset consists of 100,000 Spotify tracks sampled from a larger corpus of audio metadata.  
Each track includes musical attributes (danceability, energy, loudness, etc.), descriptive information (artist, track name, genre), and a popularity score assigned by Spotify.  

The goal of this project is to **predict a track’s popularity score** using musical and metadata features.

The dataset contains:

- **100,000 rows**
- **20 columns** (mix of numeric, categorical, and identifiers)
- **0 missing values**
- **0 duplicate rows**

This makes the dataset clean and suitable for modeling.

---

## 2. Target Variable: Popularity

The target variable is **`popularity`**, an integer ranging from 0 to 100.

### Summary Statistics

| Metric | Value |
|--------|--------|
| Mean | 18.54 |
| Std Dev | 15.93 |
| Min | 0 |
| 25th Percentile | 5 |
| Median | 15 |
| 75th Percentile | 29 |
| Max | 93 |

### Interpretation
- Popularity is **heavily skewed toward low values**, meaning most songs in the dataset are not popular.
- Popular tracks exist but are rare.
- Models must handle this skew; evaluation metrics like MAE or RMSE will be more stable than accuracy-based metrics.

---

## 3. Feature Types

### **Categorical Features**
- `genre` (82 unique genres; largest category is gospel)
- `artist_name` (high-cardinality; dropped before modeling)
- `track_name` (high-cardinality; dropped before modeling)
- `track_id` (unique; dropped)

### **Numeric Features**
- danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, year, key, mode, time_signature.

### **Index Artifact**
- `Unnamed: 0` — dropped.

---

## 4. Correlation Insights

Correlation with popularity (strongest to weakest):

| Feature | Corr w/ Popularity | Notes |
|--------|---------------------|-------|
| **year** | 0.345 | Newer songs tend to be more popular. |
| loudness | 0.106 | Louder songs slightly more popular. |
| danceability | 0.100 | Weak but useful signal. |
| instrumentalness | -0.152 | Strong negative correlation; instrumental tracks are less popular. |
| duration_ms | -0.122 | Longer tracks slightly less popular. |
| acousticness | -0.059 | Acoustic songs trend toward lower popularity. |
| liveness | -0.059 | Live tracks less popular. |
| All other features | ~0.00 | Very weak correlation individually. |

### Key Observations
- **Year** is by far the most predictive linear feature.
- Audio features have weak linear correlation but **nonlinear models may extract meaningful interactions**.
- Genre is categorical but expected to be a strong predictor after encoding.

---

## 5. Data Quality & Preprocessing Decisions

### To Drop
- `Unnamed: 0` (index artifact)
- `artist_name`, `track_name`, `track_id` (high-cardinality identifiers)
- `key`, `mode`, `time_signature` (very low predictive power)

### To Encode
- `genre` → one-hot, top-K encoding, or target encoding

### To Scale
- duration_ms  
- loudness  
- tempo (optional)

### To Keep as-is
- danceability  
- energy  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- year

---

## 6. Summary of Key Insights

- Dataset is clean (no missing data, no duplicates).
- Popularity is highly imbalanced toward low values.
- Year is the strongest single predictor.
- Instrumentalness and duration_ms have meaningful negative correlations.
- Most audio features show weak linear correlation but may be important for nonlinear ML models.
- Several low-value or high-cardinality features will be removed to simplify modeling.

This analysis provides a clear foundation for the next steps: **data cleaning, feature engineering, and model training.**
