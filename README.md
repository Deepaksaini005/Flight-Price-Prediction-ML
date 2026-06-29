# ✈️ Flight Price Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview

Flight ticket prices fluctuate based on multiple factors such as airline, source, destination, travel date, departure time, duration, and stops.

This project leverages **Machine Learning** to accurately predict flight ticket prices using historical flight data. It includes complete data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and deployment through a **Streamlit** web application.

---

## 🚀 Live Demo

🌐 **Streamlit App**

https://flight-price-prediction-ml.streamlit.app/

---

## 📂 Repository Structure

```
Flight-Price-Prediction-ML/
│
├── app.py                     # Streamlit Application
├── code.ipynb                 # Jupyter Notebook
├── Clean_Dataset.csv          # Dataset
├── flight_price_model.pkl     # Trained Model
├── encoder.pkl                # Label Encoder
├── requirements.txt           # Dependencies
└── README.md
```

---

## 🎯 Features

- Predict Flight Ticket Prices
- Interactive Streamlit Interface
- Data Preprocessing
- Feature Engineering
- Model Comparison
- Hyperparameter Tuning
- Real-time Predictions
- Easy to Use UI

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Gradient Boosting
- Random Forest
- Streamlit
- Pickle

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Encoding
6. Train-Test Split
7. Model Training
8. Hyperparameter Tuning (GridSearchCV)
9. Model Evaluation
10. Deployment with Streamlit

---

## 📈 Models Used

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

The best-performing model was selected based on evaluation metrics and deployed in the Streamlit application.

---

## 📊 Input Features

- Airline
- Source City
- Destination City
- Departure Time
- Arrival Time
- Stops
- Class
- Duration
- Days Left

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Deepaksaini005/Flight-Price-Prediction-ML.git
```

Move into the project folder

```bash
cd Flight-Price-Prediction-ML
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

> Add screenshots of your Streamlit application here.

Example:

```
images/
    home.png
    prediction.png
```

---

## 📌 Future Improvements

- Deep Learning Model
- Live Flight API Integration
- Airline Recommendation System
- Price Trend Visualization
- Model Explainability (SHAP)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Deepak Saini**

- GitHub: https://github.com/Deepaksaini005
- 
---

## ⭐ Support

If you found this project helpful,

⭐ Star this repository

and share it with others!
