import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "symptoms": [
        "itching",
        "skin_rash",
        "nodal_skin_eruptions"
    ]
}

response = requests.post(url, json=data)

print(response.json())