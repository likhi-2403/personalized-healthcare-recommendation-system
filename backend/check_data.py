import pandas as pd

print("DESCRIPTION")
df = pd.read_csv("../Dataset/description.csv")
print(df["Disease"].head(50))

print("\nMEDICATIONS")
df = pd.read_csv("../Dataset/medications.csv")
print(df["Disease"].head(50))

print("\nDIETS")
df = pd.read_csv("../Dataset/diets.csv")
print(df["Disease"].head(50))