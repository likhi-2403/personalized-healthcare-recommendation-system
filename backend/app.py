from flask import Flask, request, jsonify
from predict import predict_disease
from recommendation_engine import get_recommendations

from database import (
    save_prediction,
    get_history,
    get_analytics
)

import webbrowser
import os

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <h1>Healthcare Recommendation System API Running</h1>
    <p>Backend is running successfully.</p>
    """


@app.route("/health")
def health():

    return jsonify({
        "status": "running",
        "message": "Healthcare Recommendation System API is active"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        symptoms = data["symptoms"]

        # Disease Prediction
        disease, confidence, top_predictions = predict_disease(symptoms)

        # Save Prediction History
        save_prediction(
            disease,
            confidence
        )

        # Get Recommendations
        recommendations = get_recommendations(disease)

        response = {
            "disease": disease,
            "confidence": confidence,
            "top_predictions": top_predictions,
            "description": recommendations["description"],
            "medications": recommendations["medications"],
            "diet": recommendations["diet"],
            "precautions": recommendations["precautions"],
            "workout": recommendations["workout"]
        }

        return jsonify(response)

    except Exception as e:

        import traceback
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():

    try:

        history_data = get_history()

        result = []

        for row in history_data:

            result.append({
                "id": row[0],
                "timestamp": row[1],
                "disease": row[2],
                "confidence": row[3]
            })

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/analytics", methods=["GET"])
def analytics():

    try:

        return jsonify(
            get_analytics()
        )

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    # Open browser only once
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://127.0.0.1:5000")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )