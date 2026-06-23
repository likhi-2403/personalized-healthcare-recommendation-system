import os
import ast
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

description_df = pd.read_csv(
    os.path.join(BASE_DIR, "Dataset", "description.csv")
)

medications_df = pd.read_csv(
    os.path.join(BASE_DIR, "Dataset", "medications.csv")
)

diets_df = pd.read_csv(
    os.path.join(BASE_DIR, "Dataset", "diets.csv")
)

precautions_df = pd.read_csv(
    os.path.join(BASE_DIR, "Dataset", "precautions_df.csv")
)

workout_df = pd.read_csv(
    os.path.join(BASE_DIR, "Dataset", "workout_df.csv")
)

def get_recommendations(disease):

    print("\nPREDICTED DISEASE =", disease)

    result = {
        "description": "",
        "medications": [],
        "diet": [],
        "precautions": [],
        "workout": []
    }

def get_recommendations(disease):

    result = {
        "description": "",
        "medications": [],
        "diet": [],
        "precautions": [],
        "workout": []
    }

    # Description
    desc = description_df[
        description_df["Disease"] == disease
    ]

    if not desc.empty:
        result["description"] = desc.iloc[0]["Description"]

    # Medications
    meds = medications_df[
        medications_df["Disease"] == disease
    ]

    if not meds.empty:
        print(meds.iloc[0]["Medication"])

        result["medications"] = ast.literal_eval(
            meds.iloc[0]["Medication"]
        )

    # Diet
    diet = diets_df[
        diets_df["Disease"] == disease
    ]

    if not diet.empty:
        print(diet.iloc[0]["Diet"])

        result["diet"] = ast.literal_eval(
            diet.iloc[0]["Diet"]
        )

    # Precautions
    precaution = precautions_df[
        precautions_df["Disease"] == disease
    ]

    if not precaution.empty:

        result["precautions"] = []

        for col in [
            "Precaution_1",
            "Precaution_2",
            "Precaution_3",
            "Precaution_4"
        ]:
            value = precaution.iloc[0][col]

            if pd.notna(value):
                result["precautions"].append(str(value))


    # Workout
    workout = workout_df[
        workout_df["disease"] == disease
    ]

    if not workout.empty:
        result["workout"] = workout["workout"].tolist()

    return result