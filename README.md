# 🎧 Spotify Popularity Prediction  
**A Data Management + Machine Learning Project**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)
![Machine Learning](https://img.shields.io/badge/ML-Regression-orange)

---

## 📌 Project Overview
This project explores Spotify track data to **clean, transform, and model** musical features in order to predict a track’s popularity.  
It integrates **data management**, **database querying**, **SQL-based exploratory analysis**, and **machine learning modeling**.  
A **Streamlit application** allows users to explore the processed dataset and interact with predictions.

The project fulfills all three required components:

- **Data Management:** cleaning, feature engineering, SQLite database, SQL cluster analysis  
- **Machine Learning:** regression modeling (notebooks 03–04)  
- **Application Layer:** Streamlit GUI (`app/app.py`)  

---

## 📁 Repository Structure

```
Spotify_Popularity_Prediction-main/
│
├── app/
│   └── app.py                    # Streamlit interface
│
├── data/
│   ├── spotify.db                # SQLite database used for SQL analysis
│   ├── raw/
│   │   └── spotify_100k.csv      # Original dataset
│   └── cleaned/
│       ├── spotify_cleaned.csv
│       └── sp_dataset_for_modeling.csv
│
├── docs/
│   ├── data_dictionary.md        # Explanation of features
│   └── data_overview.md          # Dataset summary
│
├── models/
│   └── feature_columns.txt       # Columns selected for modeling
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   └── 05_sql_cluster_analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🔍 Data Pipeline

### **1. Raw Data**
Stored in:
```
data/raw/spotify_100k.csv
```

### **2. Cleaning & Preparation**  
Performed in notebooks:
- `02_data_cleaning.ipynb`
  - Remove duplicates  
  - Normalize inconsistent values  
  - Fix missing or invalid entries  

Outputs saved to:
```
data/cleaned/spotify_cleaned.csv
```

### **3. Feature Engineering**
Notebook:
- `03_feature_engineering.ipynb`

Includes:
- Selecting numerical audio features  
- Encoding categorical fields (genre, mode, key)  
- Preparing modeling dataset

Output:
```
data/cleaned/sp_dataset_for_modeling.csv
models/feature_columns.txt
```

### **4. Machine Learning Model Training**
Notebook:
- `04_modeling.ipynb`

Includes steps such as:
- Train/test split  
- Standardization  
- Model selection (e.g., Random Forest, Linear Regression, etc.)  
- Evaluation metrics (RMSE, MAE, R²)

### **5. SQL Analysis & Clustering**
Notebook:
- `05_sql_cluster_analysis.ipynb`

Uses:
```
data/spotify.db
```
Tasks performed:
- SQL queries for data exploration  
- Cluster analysis using SQL-based grouping  

---

## 🧠 Application (Streamlit App)

The Streamlit app (`app/app.py`) provides a GUI for:
- Viewing dataset summaries  
- Querying the SQLite database  
- Visualizing track distributions  
- Running model-based predictions (if included in your app logic)

---

## 🛠 Installation & Setup

### **1. Clone the Repository**
```bash
git clone <your-project-repo>
cd Spotify_Popularity_Prediction-main
```

### **2. Create a Virtual Environment(optional)**
```bash
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Verify Required Files Exist**
```bash
ls data/raw/
ls data/cleaned/
ls notebooks/
ls models/
```

---

## ▶️ Running the Streamlit App

From the project root:

```bash
streamlit run app/app.py
```

The app will open automatically in the browser at:
```
http://localhost:8501/
```

---

## 📊 Notebooks Summary

| Notebook | Purpose |
|---------|---------|
| **01_data_overview.ipynb** | Initial EDA, understanding raw dataset |
| **02_data_cleaning.ipynb** | Cleaning, handling missing data, preprocessing |
| **03_feature_engineering.ipynb** | Feature selection, encoding, dataset preparation |
| **04_modeling.ipynb** | Train ML model + evaluate performance |
| **05_sql_cluster_analysis.ipynb** | SQL analysis inside SQLite database |

---

## 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| Programming | Python |
| Database | SQLite (`spotify.db`) |
| ML Libraries | Pandas, NumPy, scikit-learn |
| Visualization | Seaborn, Matplotlib |
| Interface | Streamlit |
| Data Storage | CSV, SQLite |

---

## 🚀 Future Enhancements  
- Deploy model endpoint using FastAPI   
- Add user-upload prediction functionality in Streamlit  
- Integrate genre clustering visuals into the UI  

---

## 👥 Contributors
- Keerthana Venkatesan

---
