# Data Dictionary

| Column Name          | Type    | Description                                                                                               |
|----------------------|---------|-----------------------------------------------------------------------------------------------------------|
| Unnamed: 0           | int64   | Index artifact from the original dataset. Not useful for modeling. Will be dropped.                       |
| artist_name          | object  | Name of the performing artist. Very high-cardinality categorical feature. Not used directly for modeling. |
| track_name           | object  | Title of the song. Very high-cardinality. Not useful for modeling without NLP.                            |
| track_id             | object  | Unique Spotify track identifier. Not predictive; removed before training.                                 |
| popularity           | int64   | **Target variable.** Spotify’s popularity score (0–100).                                                  |
| year                 | int64   | Release year of the track. Newer songs tend to be more popular. Useful predictor.                         |
| genre                | object  | Genre classification for the track. Categorical feature; will be encoded.                                 |
| danceability         | float64 | Measure (0–1) of how suitable a track is for dancing based on tempo, rhythm, and beat strength.           |
| energy               | float64 | Perceived intensity and activity of the track (0–1).                                                      |
| key                  | int64   | Musical key (0–11). Weak predictor; optional for modeling.                                                |
| loudness             | float64 | Average loudness of the track in dB. Higher loudness correlates with higher popularity.                   |
| mode                 | int64   | Modality: 1 = major, 0 = minor. Very weak predictor; optional.                                            |
| speechiness          | float64 | Presence of spoken words (0–1). Weak predictor.                                                           |
| acousticness         | float64 | Confidence (0–1) that the track is acoustic. Negatively correlated with popularity.                       |
| instrumentalness     | float64 | Predicts whether vocals are present (0–1). Strong negative correlation with popularity.                   |
| liveness             | float64 | Likelihood (0–1) that the track was performed live. Weak predictor.                                       |
| valence              | float64 | Musical positivity/happiness (0–1). Weak predictor.                                                       |
| tempo                | float64 | Estimated tempo (BPM). Very weak predictor; optional.                                                     |
| duration_ms          | int64   | Duration of the track in milliseconds. Moderately correlated with popularity.                             |
| time_signature       | int64   | Estimated time signature (e.g., 3, 4, 5). Weak predictor; optional.                                       |
