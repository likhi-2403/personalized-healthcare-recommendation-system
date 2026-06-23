import streamlit as st
import time
import random
import requests

# ── Sample Data (backend teammate will replace with real ML model) ───────────
SYMPTOMS = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
    "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue",
    "vomiting", "burning_micturition", "fatigue", "weight_gain", "anxiety",
    "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
    "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
    "breathlessness", "sweating", "dehydration", "indigestion", "headache",
    "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "pain_behind_eyes",
    "back_pain", "constipation", "abdominal_pain", "diarrhoea", "mild_fever",
    "yellow_urine", "yellowing_of_eyes", "chest_pain", "fast_heart_rate", "neck_pain",
    "dizziness", "cramps", "bruising", "obesity", "swollen_legs",
    "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremities",
    "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips",
    "slurred_speech", "knee_pain", "hip_joint_pain", "muscle_weakness", "stiff_neck",
    "swelling_joints", "movement_stiffness", "spinning_movements", "loss_of_balance",
    "unsteadiness", "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort",
    "continuous_feel_of_urine", "passage_of_gases", "internal_itching",
    "toxic_look_(typhos)", "depression", "irritability", "muscle_pain", "altered_sensorium",
    "red_spots_over_body", "belly_pain", "abnormal_menstruation", "watering_from_eyes",
    "increased_appetite", "polyuria", "family_history", "mucoid_sputum", "rusty_sputum",
    "lack_of_concentration", "visual_disturbances", "receiving_blood_transfusion",
    "receiving_unsterile_injections", "coma", "stomach_bleeding", "distention_of_abdomen",
    "history_of_alcohol_consumption", "blood_in_sputum", "prominent_veins_on_calf",
    "palpitations", "painful_walking", "pus_filled_pimples", "blackheads", "scurring",
    "skin_peeling", "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails",
    "blister", "red_sore_around_nose", "yellow_crust_ooze",
]

DISEASES = {
    "Fungal Infection":     ("🍄", "#FF6B6B", ["itching", "skin_rash", "nodal_skin_eruptions"]),
    "Common Cold":          ("🤧", "#4ECDC4", ["continuous_sneezing", "shivering", "chills", "fatigue", "cough"]),
    "Diabetes":             ("💉", "#45B7D1", ["excessive_hunger", "polyuria", "weight_loss", "fatigue", "increased_appetite"]),
    "Hypertension":         ("❤️", "#F7DC6F", ["headache", "chest_pain", "dizziness", "fatigue", "breathlessness"]),
    "Migraine":             ("🧠", "#BB8FCE", ["headache", "nausea", "vomiting", "pain_behind_eyes", "dizziness"]),
    "Typhoid":              ("🤒", "#F0B27A", ["high_fever", "headache", "nausea", "vomiting", "abdominal_pain"]),
    "Malaria":              ("🦟", "#82E0AA", ["chills", "high_fever", "headache", "nausea", "sweating", "fatigue"]),
    "Dengue":               ("🌡️", "#F1948A", ["high_fever", "headache", "pain_behind_eyes", "joint_pain", "skin_rash"]),
    "Jaundice":             ("😷", "#FAD7A0", ["itching", "vomiting", "fatigue", "weight_loss", "high_fever", "dark_urine", "yellowish_skin"]),
    "Pneumonia":            ("🫁", "#AED6F1", ["cough", "high_fever", "breathlessness", "chest_pain", "fatigue", "sweating"]),
}

PRECAUTIONS = {
    "Fungal Infection":  ["Keep skin clean and dry", "Use antifungal cream", "Avoid sharing personal items", "Wear breathable clothing"],
    "Common Cold":       ["Rest and drink fluids", "Use a humidifier", "Wash hands frequently", "Avoid close contact with others"],
    "Diabetes":          ["Monitor blood sugar regularly", "Follow a healthy diet", "Exercise daily", "Take medication as prescribed"],
    "Hypertension":      ["Reduce salt intake", "Exercise regularly", "Avoid smoking and alcohol", "Monitor blood pressure daily"],
    "Migraine":          ["Rest in a dark quiet room", "Stay hydrated", "Avoid trigger foods", "Manage stress levels"],
    "Typhoid":           ["Drink purified water only", "Eat freshly cooked food", "Maintain hygiene", "Complete antibiotic course"],
    "Malaria":           ["Use mosquito nets", "Apply mosquito repellent", "Take antimalarial drugs", "Avoid stagnant water areas"],
    "Dengue":            ["Use mosquito repellent", "Wear full sleeves", "Stay hydrated", "Rest and monitor platelet count"],
    "Jaundice":          ["Avoid fatty foods", "Rest completely", "Stay hydrated", "Avoid alcohol strictly"],
    "Pneumonia":         ["Complete antibiotic course", "Rest and sleep well", "Stay warm", "Drink plenty of fluids"],
}

def predict_disease(symptoms):

    try:

        url = "http://127.0.0.1:5000/predict"

        payload = {
            "symptoms": symptoms
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:

            result = response.json()

            return (
                result["disease"],
                result["confidence"],
                result
            )

        return None, 0, None

    except Exception as e:
        st.error(f"API Error: {e}")
        return None, 0, None

def show():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }

.symptom-chip {
    display: inline-block;
    background: #E1F5EE;
    color: #0B7285;
    border: 1.5px solid #0B7285;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    margin: 3px;
    cursor: pointer;
}
.symptom-chip-selected {
    display: inline-block;
    background: #0B7285;
    color: white;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    margin: 3px;
}
div[data-testid="stTextInput"] > div > div > input {
    border-radius: 10px !important;
    border: 1.5px solid #e0e0e0 !important;
    padding: 10px 14px !important;
    font-size: 13px !important;
}
div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #0B7285 !important;
    box-shadow: 0 0 0 3px rgba(11,114,133,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

    # Session state for symptoms
    if "selected_symptoms" not in st.session_state:
        st.session_state.selected_symptoms = []
    if "prediction_result" not in st.session_state:
        st.session_state.prediction_result = None
    if "prediction_confidence" not in st.session_state:
        st.session_state.prediction_confidence = 0
    if "api_result" not in st.session_state:
        st.session_state.api_result = None

    # ── PAGE HEADER ───────────────────────────────────────────────────────
    st.markdown("""
<div style="background:linear-gradient(135deg,#0B7285 0%,#1aabbd 100%);
            border-radius:16px;padding:32px 36px;margin-bottom:24px;
            display:flex;align-items:center;gap:20px;">
  <div style="font-size:48px;">🩺</div>
  <div>
    <div style="font-size:22px;font-weight:700;color:#fff;">Disease Prediction</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-top:4px;">
      Select your symptoms below and let our AI predict the most likely condition
    </div>
  </div>
  <div style="margin-left:auto;background:rgba(255,255,255,0.12);border-radius:12px;padding:12px 20px;text-align:center;">
    <div style="font-size:22px;font-weight:700;color:#fff;">92%</div>
    <div style="font-size:10px;color:rgba(255,255,255,0.6);">Accuracy</div>
  </div>
</div>
""", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.2, 1], gap="large")

    # ── LEFT: SYMPTOM SELECTOR ────────────────────────────────────────────
    with left_col:

        st.markdown('<div style="font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:12px;">🔍 Search & Select Symptoms</div>', unsafe_allow_html=True)

        search = st.text_input("", placeholder="Type a symptom e.g. headache, fever, cough...", key="symptom_search", label_visibility="collapsed")

        # Filter symptoms based on search
        filtered = [s for s in SYMPTOMS if search.lower().replace(" ", "_") in s] if search else SYMPTOMS[:60]

        st.markdown('<div style="font-size:11px;color:#999;margin-bottom:8px;">Click a symptom to select it:</div>', unsafe_allow_html=True)

        # Show symptoms as buttons in a grid
        st.markdown('<div style="background:#f9f9f9;border-radius:12px;padding:14px;max-height:280px;overflow-y:auto;border:1px solid #eee;">', unsafe_allow_html=True)

        # Display in rows of 3
        symptoms_to_show = filtered[:30]
        rows = [symptoms_to_show[i:i+3] for i in range(0, len(symptoms_to_show), 3)]

        for row in rows:
            cols = st.columns(3)
            for col, symptom in zip(cols, row):
                with col:
                    label = symptom.replace("_", " ").title()
                    is_selected = symptom in st.session_state.selected_symptoms
                    btn_style = "✅ " if is_selected else ""
                    if st.button(f"{btn_style}{label}", key=f"sym_{symptom}", use_container_width=True):
                        if symptom in st.session_state.selected_symptoms:
                            st.session_state.selected_symptoms.remove(symptom)
                        else:
                            st.session_state.selected_symptoms.append(symptom)
                        st.session_state.prediction_result = None
                        st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        # Selected symptoms display
        st.markdown('<div style="margin-top:16px;font-size:13px;font-weight:600;color:#1a1a1a;">Selected Symptoms:</div>', unsafe_allow_html=True)

        if st.session_state.selected_symptoms:
            chips_html = ""
            for s in st.session_state.selected_symptoms:
                chips_html += f'<span class="symptom-chip-selected">{s.replace("_"," ").title()} ✕</span>'
            st.markdown(f'<div style="margin-top:8px;padding:12px;background:#fff;border-radius:10px;border:1px solid #eee;">{chips_html}</div>', unsafe_allow_html=True)

            col_predict, col_clear = st.columns([2, 1])
            with col_predict:
                if st.button("🔍  Predict Disease", use_container_width=True, key="predict_btn"):

                    with st.spinner("Analyzing your symptoms..."):
                        time.sleep(1)

                    disease, confidence, result = predict_disease(
                        st.session_state.selected_symptoms
                    )

                    st.session_state.api_result = result
                    st.session_state.prediction_result = disease
                    st.session_state.prediction_confidence = confidence

                    st.rerun()

            with col_clear:
                if st.button("🗑️  Clear All", use_container_width=True, key="clear_btn"):
                    st.session_state.selected_symptoms = []
                    st.session_state.prediction_result = None
                    st.rerun()
        else:
            st.markdown(
                '<div style="margin-top:8px;padding:16px;background:#f9f9f9;border-radius:10px;'
                'border:1px dashed #ddd;text-align:center;color:#aaa;font-size:12px;">'
                'No symptoms selected yet. Click symptoms above to add them.</div>',
                unsafe_allow_html=True,
            )

    # ── RIGHT: RESULT PANEL ───────────────────────────────────────────────
    with right_col:
        st.markdown('<div style="font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:12px;">📊 Prediction Result</div>', unsafe_allow_html=True)

        if st.session_state.prediction_result:
            disease = st.session_state.prediction_result
            confidence = st.session_state.prediction_confidence
            icon, color, _ = DISEASES.get(disease, ("🏥", "#0B7285", []))
            precautions = []

            if st.session_state.api_result:
                precautions = st.session_state.api_result.get(
                    "precautions",
                    []
                )

            # Result card
            st.markdown(f"""
<div style="background:linear-gradient(135deg,{color}22,{color}11);
            border:2px solid {color}44;border-radius:16px;padding:24px;margin-bottom:16px;">
  <div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
    <div style="font-size:44px;">{icon}</div>
    <div>
      <div style="font-size:11px;color:#888;font-weight:500;text-transform:uppercase;letter-spacing:1px;">Predicted Condition</div>
      <div style="font-size:22px;font-weight:700;color:#1a1a1a;margin-top:2px;">{disease}</div>
    </div>
  </div>
  <div style="font-size:12px;color:#666;margin-bottom:8px;font-weight:500;">Confidence Score</div>
  <div style="display:flex;align-items:center;gap:10px;">
    <div style="flex:1;background:#e0e0e0;border-radius:6px;height:8px;">
      <div style="background:{color};width:{confidence}%;height:8px;border-radius:6px;"></div>
    </div>
    <div style="font-size:16px;font-weight:700;color:{color};">{confidence}%</div>
  </div>
</div>
""", unsafe_allow_html=True)

            # Symptoms matched
            st.markdown(f"""
<div style="background:#fff;border:1px solid #eee;border-radius:12px;padding:16px;margin-bottom:16px;">
  <div style="font-size:13px;font-weight:600;color:#1a1a1a;margin-bottom:10px;">✅ Symptoms Analyzed</div>
  <div style="font-size:12px;color:#666;">
    You selected <b>{len(st.session_state.selected_symptoms)}</b> symptom(s). Our model matched them against 40+ conditions.
  </div>
</div>
""", unsafe_allow_html=True)

            # Precautions
            st.markdown('<div style="background:#fff;border:1px solid #eee;border-radius:12px;padding:16px;margin-bottom:16px;">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:13px;font-weight:600;color:#1a1a1a;margin-bottom:12px;">⚠️ Recommended Precautions</div>', unsafe_allow_html=True)
            for i, p in enumerate(precautions, 1):
                st.markdown(
                    f'<div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:8px;">'
                    f'<div style="width:22px;height:22px;background:#E1F5EE;border-radius:50%;'
                    f'display:flex;align-items:center;justify-content:center;'
                    f'font-size:11px;font-weight:700;color:#0B7285;flex-shrink:0;">{i}</div>'
                    f'<div style="font-size:12px;color:#555;padding-top:3px;">{p}</div></div>',
                    unsafe_allow_html=True,
                )
            st.markdown('</div>', unsafe_allow_html=True)

            if st.session_state.api_result:

                result = st.session_state.api_result


                # Top Predictions

                if "top_predictions" in result:

                    st.markdown("### 🎯 Top 3 Predictions")

                    for pred in result["top_predictions"]:

                        st.write(
                            f"• {pred['disease']} ({pred['confidence']}%)"
                        )

                st.markdown("### 💊 Medicines")

                for med in result["medications"]:
                    st.write("•", med)

                st.markdown("### 🥗 Diet")

                for item in result["diet"]:
                    st.write("•", item)

                st.markdown("### 🏋 Workout")

                for item in result["workout"]:
                    st.write("•", item)

                st.markdown("### 📄 Description")

                st.info(result["description"])

            # Disclaimer
            st.markdown("""
<div style="background:#FFF9E6;border:1px solid #F7DC6F;border-radius:10px;padding:12px 14px;">
  <div style="font-size:11px;color:#856404;">
    ⚠️ <b>Disclaimer:</b> This prediction is AI-generated and for informational purposes only.
    Please consult a qualified medical professional for proper diagnosis and treatment.
  </div>
</div>
""", unsafe_allow_html=True)

            # Action buttons
            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("💊  Get Medicines", use_container_width=True, key="goto_medicine"):
                    st.session_state.page = "medicine"
                    st.rerun()
            with c2:
                if st.button("🥗  Get Diet Plan", use_container_width=True, key="goto_diet"):
                    st.session_state.page = "diet"
                    st.rerun()

        else:
            # Empty state
            st.markdown("""
<div style="background:#f9f9f9;border:1px dashed #ddd;border-radius:16px;
            padding:48px 24px;text-align:center;">
  <div style="font-size:48px;margin-bottom:16px;">🔬</div>
  <div style="font-size:15px;font-weight:600;color:#888;margin-bottom:8px;">No Prediction Yet</div>
  <div style="font-size:12px;color:#bbb;line-height:1.7;">
    Select at least 3 symptoms from the left panel<br>and click <b>Predict Disease</b> to get started.
  </div>
</div>
""", unsafe_allow_html=True)

            # Tips
            st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
            st.markdown("""
<div style="background:#fff;border:1px solid #eee;border-radius:12px;padding:16px;">
  <div style="font-size:13px;font-weight:600;color:#1a1a1a;margin-bottom:10px;">💡 Tips for better results</div>
  <div style="font-size:12px;color:#666;line-height:1.9;">
    • Select <b>3 or more symptoms</b> for accurate prediction<br>
    • Use the search bar to find symptoms quickly<br>
    • Be as specific as possible with your symptoms<br>
    • Check the confidence score after prediction
  </div>
</div>
""", unsafe_allow_html=True)