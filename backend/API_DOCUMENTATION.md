# Healthcare Recommendation System API

## Base URL

http://127.0.0.1:5000

---

## Health Check

### Request

GET /health

### Response


{
  "status": "running",
  "message": "Healthcare Recommendation System API is active"
}


---

## Disease Prediction & Recommendation

### Request

POST /predict

### Body


{
  "symptoms": [
    "itching",
    "skin_rash",
    "nodal_skin_eruptions"
  ]
}


### Response

{
  "disease": "Fungal infection",
  "confidence": 100.0,
  "description": "Fungal infection is a common skin condition caused by fungi.",
  "medications": [
    "Antifungal Cream",
    "Fluconazole",
    "Terbinafine"
  ],
  "diet": [
    "Antifungal Diet",
    "Probiotics",
    "Garlic"
  ],
  "precautions": [
    "bath twice",
    "use detol or neem in bathing water",
    "keep infected area dry",
    "use clean cloths"
  ],
  "workout": [
    "Avoid sugary foods",
    "Consume probiotics"
  ]
}

