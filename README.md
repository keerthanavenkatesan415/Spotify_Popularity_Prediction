# 🎧 Spotify Track Popularity Prediction  
**Machine Learning · Data Management · Streamlit App**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Model](https://img.shields.io/badge/ML-Regression%20Model-orange.svg)]()

---

### 📌 Project Overview
This project predicts the popularity of Spotify tracks using a combination of **machine learning**, **data preprocessing**, and an **interactive Streamlit user interface**.  
Users can upload track features or explore preloaded song data to see predicted popularity values based on a trained ML model.

The project integrates the core components required for a Data Management course project:

- **Database / Data Management:** data ingestion, cleaning, feature processing  
- **Machine Learning:** regression modeling + evaluation  
- **Application Layer:** Streamlit GUI for interacting with predictions  

---

## 🗂 Repository Structure

```
Spotify_Popularity_Prediction-main/
│
├── app/                     # Streamlit user interface
│   ├── app.py
│   └── utils.py
│
├── data/                    # Raw & processed datasets
│   ├── raw_tracks.csv
│   └── processed_tracks.csv
│
├── models/                  # Trained ML models & scalers
│   ├── model.pkl
│   └── scaler.pkl
│
├── notebooks/               # Jupyter notebooks (EDA, preprocessing, training)
│   ├── 1_data_cleaning.ipynb
│   ├── 2_feature_engineering.ipynb
│   └── 3_model_training.ipynb
│
├── docs/                    # Documentation and report materials
│
├── requirements.txt
└── README.md                # (this file)
```

---

## 🧠 ML Pipeline Overview

### System Architecture  
```
Raw Dataset → Preprocessing → Feature Encoding & Scaling → Model Training → Streamlit App
```

### Main Components
- **Data Cleaning:** handle nulls, remove duplicates, normalize inconsistent fields  
- **Feature Engineering:**  
  - Genre encoding  
  - Numerical scaling using StandardScaler  
- **Modeling:**  
  - Regression model (Random Forest / XGBoost depending on final notebook)  
- **Evaluation:**  
  - RMSE, MAE, R²  
- **Deployment:**  
  - Streamlit-based interactive UI  
  - Model + scaler loaded from /models  

---

## 🚀 Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/Spotify_Popularity_Prediction.git
cd Spotify_Popularity_Prediction
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Verify That Model + Scaler Exist**
```bash
ls models/
# Should show: model.pkl  scaler.pkl
```

If missing, re-run the training notebook inside `/notebooks`.

---

## ▶️ Running the Application

### **Start the Streamlit App**
From the project root:

```bash
streamlit run app/app.py
```

After launching, open the link (usually http://localhost:8501/) to begin using the prediction interface.

---

## 🖥️ Streamlit App Features

### **1. Upload Track Features**
- Upload a `.csv` or manually input feature fields  
- App preprocesses the input using the stored scaler  
- Model predicts the track popularity score  

### **2. Explore Sample Dataset**
- Filter tracks by genre, year, acousticness, energy, etc.  
- Visualize distributions and correlations  

### **3. View Model Metrics**
- RMSE, MAE, R² scores displayed in UI  
- Comparison against baseline models  

### **4. Download Prediction Outputs**
- Export predicted results as CSV  

---

## 📊 Example Prediction Workflow

1. User uploads track features:
```csv
danceability,energy,key,loudness,speechiness,acousticness,valence,tempo
0.62,0.75,5,-6.2,0.04,0.12,0.55,120
```

2. Streamlit encodes & scales features  
3. Model outputs:
```
Predicted Popularity: 68.4 / 100
```

---

## 📘 Notebooks Included

### ✔ 1_data_cleaning.ipynb
- Remove invalid rows  
- Standardize categorical fields  
- Save cleaned dataset  

### ✔ 2_feature_engineering.ipynb
- One-hot encode genres  
- Scale numerical variables  
- Create final ML-ready dataset  

### ✔ 3_model_training.ipynb
- Compare multiple regressors  
- Train final model + save .pkl  
- Generate evaluation visualizations  

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Programming | Python 3.10 |
| ML Library | scikit-learn |
| UI | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Storage | Pickled models + CSV datasets |

---

## 📈 Future Improvements
- Add a PostgreSQL or SQLite backend  
- Deploy Streamlit using Streamlit Cloud or Docker  
- Experiment with neural models (MLP or TabNet)  
- Enhance interpretability: SHAP or LIME visualizations  

---

## 👨‍💻 Contributors
- **Your Name** – ML Engineer & Frontend Developer  
- Any additional teammates here  

---

## 📄 License
This project is licensed under the **MIT License**.

---

## ⭐ If you use this project, star the repository to support development!
