# 🩺 Personalized Healthcare & Medicine Recommendation System

## 📌 Project Overview

The Personalized Healthcare & Medicine Recommendation System is an AI-powered healthcare application that predicts diseases based on user symptoms and provides personalized recommendations including medicines, diet plans, workouts, precautions, and disease descriptions.

The system uses Machine Learning techniques to analyze symptoms and predict the most likely disease with a confidence score. It also stores prediction history and provides healthcare recommendations to assist users in understanding their health conditions.

---

## 🚀 Features

### Disease Prediction

* Predicts diseases from selected symptoms
* Uses a trained Random Forest Machine Learning model
* Displays prediction confidence score
* Shows Top 3 probable diseases

### Medicine Recommendations

* Suggests medications based on predicted disease
* Displays multiple medicine options

### Diet Recommendations

* Provides disease-specific diet plans
* Suggests healthy foods and nutritional guidance

### Workout Recommendations

* Recommends physical activities and lifestyle improvements
* Provides health-focused exercise suggestions

### Precautions

* Displays important preventive measures
* Helps users reduce health risks

### Disease Description

* Provides detailed information about predicted diseases

### History Tracking

* Stores prediction history
* Enables review of previous predictions

### Analytics Dashboard

* Displays healthcare prediction statistics
* Visual representation of prediction data

---

## 🏗️ System Architecture

Frontend (Streamlit)

↓

Flask REST API Backend

↓

Machine Learning Model (Random Forest)

↓

Recommendation Engine

↓

SQLite Database

---

## 🛠️ Technologies Used

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Pandas
* NumPy
* Joblib

### Database

* SQLite

### Development Tools

* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
Personalized Healthcare & Medicine Recommendation System/

│
├── backend/
│   ├── app.py
│   ├── predict.py
│   ├── recommendation_engine.py
│   ├── database.py
│   ├── train_model.py
│   ├── healthcare.db
│   └── requirements.txt
│
├── Frontend/
│   ├── app.py
│   └── pages/
│       ├── home.py
│       ├── login.py
│       ├── signup.py
│       ├── disease.py
│       ├── medicine.py
│       ├── diet.py
│       ├── dashboard.py
│       ├── history.py
│       └── report.py
│
├── Dataset/
│   ├── Training.csv
│   ├── description.csv
│   ├── medications.csv
│   ├── diets.csv
│   ├── precautions_df.csv
│   └── workout_df.csv
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/healthcare-recommendation-system.git
```

### Navigate to Project

```bash
cd healthcare-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

Open Terminal:

```bash
cd backend
python app.py
```

Backend will run at:

```text
http://127.0.0.1:5000
```

---

## ▶️ Run Frontend

Open another terminal:

```bash
cd Frontend
streamlit run app.py
```

Frontend will run at:

```text
http://localhost:8501
```

---

## 🧠 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Workflow

1. Load symptom dataset
2. Train Random Forest model
3. Save trained model using Joblib
4. Receive symptoms from user
5. Predict disease
6. Calculate confidence score
7. Generate recommendations
8. Display results

---

## 📊 Sample Prediction Output

### Input Symptoms

* Itching
* Skin Rash
* Nodal Skin Eruptions

### Predicted Disease

Fungal Infection

### Confidence Score

57.02%

### Recommendations

#### Medicines

* Antifungal Cream
* Fluconazole
* Terbinafine
* Clotrimazole
* Ketoconazole

#### Diet

* Antifungal Diet
* Probiotics
* Garlic
* Coconut Oil
* Turmeric

#### Workout

* Stay Hydrated
* Consume Green Tea
* Eat Fruits and Vegetables

#### Precautions

* Bath Twice Daily
* Keep Infected Area Dry
* Use Clean Clothes
* Use Neem Water

---

## 🎯 Future Enhancements

* AI Chatbot Integration
* Doctor Consultation Module
* Medical Report Upload
* Cloud Deployment
* User Authentication
* Mobile Application
* Real-Time Health Monitoring

---

## 📈 Project Outcomes

* Accurate disease prediction
* Personalized healthcare recommendations
* Improved healthcare awareness
* User-friendly healthcare assistance
* Data-driven decision support

---


## 📜 License

This project is developed for educational and internship purposes.

---

## ⚠️ Disclaimer

This application provides AI-generated healthcare recommendations for informational purposes only. It should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.
