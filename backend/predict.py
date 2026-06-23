import os
import pandas as pd
import joblib

# =========================
# Base Project Directory
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# =========================
# Paths
# =========================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "disease_model.pkl"
)

TRAINING_PATH = os.path.join(
    BASE_DIR,
    "Dataset",
    "Training.csv"
)

# =========================
# Load Model
# =========================

model = joblib.load(MODEL_PATH)

# =========================
# Load Dataset
# =========================

training_data = pd.read_csv(TRAINING_PATH)

# All symptom columns except prognosis
symptom_columns = training_data.columns[:-1]

# =========================
# Prediction Function
# =========================

def predict_disease(user_symptoms):

    input_vector = [0] * len(symptom_columns)

    for symptom in user_symptoms:

        symptom = symptom.strip()

        if symptom in symptom_columns:

            idx = list(symptom_columns).index(symptom)

            input_vector[idx] = 1

    probabilities = model.predict_proba([input_vector])[0]

    classes = model.classes_

    top_indices = probabilities.argsort()[-3:][::-1]

    top_predictions = []

    for idx in top_indices:
        top_predictions.append({
            "disease": classes[idx],
            "confidence": round(probabilities[idx] * 100, 2)
     })

    best_prediction = top_predictions[0]["disease"]
    best_confidence = round(
        min(
            95,
            top_predictions[0]["confidence"] * 2
        ),
        2
    )  

    return best_prediction, best_confidence, top_predictions 