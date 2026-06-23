from predict import predict_disease
from recommendation_engine import get_recommendations

symptoms = [
    "itching",
    "skin_rash",
    "nodal_skin_eruptions"
]

disease, confidence = predict_disease(symptoms)

print("\nDisease:")
print(disease)

print("\nConfidence:")
print(str(confidence) + "%")

print("\nRecommendations:")
print(get_recommendations(disease))