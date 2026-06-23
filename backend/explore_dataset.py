import pandas as pd

files = [
    "Dataset/description.csv",
    "Dataset/medications.csv",
    "Dataset/diets.csv",
    "Dataset/precautions_df.csv",
    "Dataset/workout_df.csv"
]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(file)

    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())