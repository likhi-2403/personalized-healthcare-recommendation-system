import streamlit as st
import time

# ── Sample Data (backend teammate replaces this with real DB / model) ────────
MEDICINE_DB = {
    "Fungal Infection": {
        "icon": "🍄", "color": "#FF6B6B",
        "medicines": [
            {"name": "Clotrimazole Cream", "type": "Topical", "dosage": "Apply 2x daily for 2 weeks", "otc": True},
            {"name": "Fluconazole",        "type": "Oral Tablet", "dosage": "150mg once weekly", "otc": False},
            {"name": "Terbinafine Cream",  "type": "Topical", "dosage": "Apply once daily for 1-2 weeks", "otc": True},
        ],
    },
    "Common Cold": {
        "icon": "🤧", "color": "#4ECDC4",
        "medicines": [
            {"name": "Paracetamol",        "type": "Oral Tablet", "dosage": "500mg every 6 hours as needed", "otc": True},
            {"name": "Cetirizine",         "type": "Oral Tablet", "dosage": "10mg once daily", "otc": True},
            {"name": "Vitamin C Syrup",    "type": "Syrup", "dosage": "10ml twice daily", "otc": True},
        ],
    },
    "Diabetes": {
        "icon": "💉", "color": "#45B7D1",
        "medicines": [
            {"name": "Metformin",          "type": "Oral Tablet", "dosage": "500mg twice daily with meals", "otc": False},
            {"name": "Glimepiride",        "type": "Oral Tablet", "dosage": "1-2mg once daily before breakfast", "otc": False},
            {"name": "Insulin (as advised)", "type": "Injection", "dosage": "As prescribed by physician", "otc": False},
        ],
    },
    "Hypertension": {
        "icon": "❤️", "color": "#F7DC6F",
        "medicines": [
            {"name": "Amlodipine",         "type": "Oral Tablet", "dosage": "5mg once daily", "otc": False},
            {"name": "Losartan",           "type": "Oral Tablet", "dosage": "50mg once daily", "otc": False},
            {"name": "Hydrochlorothiazide","type": "Oral Tablet", "dosage": "12.5mg once daily", "otc": False},
        ],
    },
    "Migraine": {
        "icon": "🧠", "color": "#BB8FCE",
        "medicines": [
            {"name": "Sumatriptan",        "type": "Oral Tablet", "dosage": "50-100mg at onset of migraine", "otc": False},
            {"name": "Ibuprofen",          "type": "Oral Tablet", "dosage": "400mg every 6-8 hours as needed", "otc": True},
            {"name": "Propranolol",        "type": "Oral Tablet", "dosage": "40mg twice daily (preventive)", "otc": False},
        ],
    },
    "Typhoid": {
        "icon": "🤒", "color": "#F0B27A",
        "medicines": [
            {"name": "Ciprofloxacin",      "type": "Oral Tablet", "dosage": "500mg twice daily for 10-14 days", "otc": False},
            {"name": "Azithromycin",       "type": "Oral Tablet", "dosage": "500mg once daily for 7 days", "otc": False},
            {"name": "ORS Solution",       "type": "Oral Solution", "dosage": "As needed for hydration", "otc": True},
        ],
    },
    "Malaria": {
        "icon": "🦟", "color": "#82E0AA",
        "medicines": [
            {"name": "Chloroquine",        "type": "Oral Tablet", "dosage": "As prescribed based on weight", "otc": False},
            {"name": "Artemether-Lumefantrine", "type": "Oral Tablet", "dosage": "As prescribed by physician", "otc": False},
            {"name": "Paracetamol",        "type": "Oral Tablet", "dosage": "500mg every 6 hours for fever", "otc": True},
        ],
    },
    "Dengue": {
        "icon": "🌡️", "color": "#F1948A",
        "medicines": [
            {"name": "Paracetamol",        "type": "Oral Tablet", "dosage": "500mg every 6 hours (avoid aspirin/ibuprofen)", "otc": True},
            {"name": "ORS Solution",       "type": "Oral Solution", "dosage": "Frequent small sips for hydration", "otc": True},
            {"name": "Platelet support care", "type": "Medical supervision", "dosage": "As advised by physician", "otc": False},
        ],
    },
    "Jaundice": {
        "icon": "😷", "color": "#FAD7A0",
        "medicines": [
            {"name": "Ursodeoxycholic acid", "type": "Oral Tablet", "dosage": "As prescribed by physician", "otc": False},
            {"name": "Multivitamin Supplement", "type": "Oral Tablet", "dosage": "Once daily", "otc": True},
            {"name": "Liver support care",  "type": "Medical supervision", "dosage": "Rest + low-fat diet", "otc": False},
        ],
    },
    "Pneumonia": {
        "icon": "🫁", "color": "#AED6F1",
        "medicines": [
            {"name": "Amoxicillin",        "type": "Oral Tablet", "dosage": "500mg three times daily for 7 days", "otc": False},
            {"name": "Azithromycin",       "type": "Oral Tablet", "dosage": "500mg once daily for 5 days", "otc": False},
            {"name": "Paracetamol",        "type": "Oral Tablet", "dosage": "500mg every 6 hours for fever", "otc": True},
        ],
    },
}


def show():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
</style>
""", unsafe_allow_html=True)

    if "my_medicine_list" not in st.session_state:
        st.session_state.my_medicine_list = []
    if "selected_condition" not in st.session_state:
        st.session_state.selected_condition = None

    # Auto-fill from disease prediction page if available
    if st.session_state.get("prediction_result") and not st.session_state.selected_condition:
        if st.session_state.prediction_result in MEDICINE_DB:
            st.session_state.selected_condition = st.session_state.prediction_result

    # ── HEADER ────────────────────────────────────────────────────────────
    st.markdown("""
<div style="background:linear-gradient(135deg,#0B7285 0%,#1aabbd 100%);
            border-radius:16px;padding:32px 36px;margin-bottom:24px;
            display:flex;align-items:center;gap:20px;">
  <div style="font-size:48px;">💊</div>
  <div>
    <div style="font-size:22px;font-weight:700;color:#fff;">Medicine Recommendation</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-top:4px;">
      Select a condition to get personalised medicine suggestions
    </div>
  </div>
  <div style="margin-left:auto;background:rgba(255,255,255,0.15);border-radius:12px;padding:12px 20px;text-align:center;">
    <div style="font-size:22px;font-weight:700;color:#fff;">500+</div>
    <div style="font-size:10px;color:rgba(255,255,255,0.6);">Medicines mapped</div>
  </div>
</div>
""", unsafe_allow_html=True)

    if st.session_state.get("prediction_result") and st.session_state.selected_condition == st.session_state.prediction_result:
        st.markdown(
            f'<div style="background:#E1F5EE;border:1px solid #b2dfdb;border-radius:10px;'
            f'padding:10px 16px;margin-bottom:18px;font-size:12px;color:#0B7285;">'
            f'✨ Auto-filled from your recent prediction: <b>{st.session_state.prediction_result}</b></div>',
            unsafe_allow_html=True,
        )

    left_col, right_col = st.columns([1, 1.3], gap="large")

    # ── LEFT: CONDITION SELECTOR ──────────────────────────────────────────
    with left_col:
        st.markdown('<div style="font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:12px;">Select a Condition</div>', unsafe_allow_html=True)

        conditions = list(MEDICINE_DB.keys())
        rows = [conditions[i:i+2] for i in range(0, len(conditions), 2)]

        for row in rows:
            cols = st.columns(2)
            for col, cond in zip(cols, row):
                with col:
                    data = MEDICINE_DB[cond]
                    is_selected = st.session_state.selected_condition == cond
                    border = f"2px solid {data['color']}" if is_selected else "1px solid #eee"
                    bg = f"{data['color']}15" if is_selected else "#fff"

                    st.markdown(
                        f'<div style="background:{bg};border:{border};border-radius:12px;'
                        f'padding:14px;text-align:center;margin-bottom:6px;">'
                        f'<div style="font-size:28px;margin-bottom:6px;">{data["icon"]}</div>'
                        f'<div style="font-size:12px;font-weight:600;color:#1a1a1a;">{cond}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                    if st.button("Select" if not is_selected else "✓ Selected", key=f"med_cond_{cond}", use_container_width=True):
                        st.session_state.selected_condition = cond
                        st.rerun()

        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        # My medicine list
        if st.session_state.my_medicine_list:
            st.markdown('<div style="font-size:14px;font-weight:600;color:#1a1a1a;margin-top:20px;margin-bottom:10px;">📋 My Medicine List</div>', unsafe_allow_html=True)
            st.markdown('<div style="background:#fff;border:1px solid #eee;border-radius:12px;padding:14px;">', unsafe_allow_html=True)
            for i, med in enumerate(st.session_state.my_medicine_list):
                col_a, col_b = st.columns([4, 1])
                with col_a:
                    st.markdown(f'<div style="font-size:12px;color:#333;padding:6px 0;">💊 {med}</div>', unsafe_allow_html=True)
                with col_b:
                    if st.button("✕", key=f"remove_med_{i}"):
                        st.session_state.my_medicine_list.pop(i)
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # ── RIGHT: MEDICINE DETAILS ───────────────────────────────────────────
    with right_col:
        if st.session_state.selected_condition:
            cond = st.session_state.selected_condition
            data = MEDICINE_DB[cond]

            st.markdown(f"""
<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
  <div style="font-size:36px;">{data['icon']}</div>
  <div>
    <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;">Recommended for</div>
    <div style="font-size:20px;font-weight:700;color:#1a1a1a;">{cond}</div>
  </div>
</div>
""", unsafe_allow_html=True)

            for med in data["medicines"]:
                otc_badge = (
                    '<span style="background:#E1F5EE;color:#0B7285;font-size:10px;font-weight:600;'
                    'padding:3px 10px;border-radius:12px;">OTC</span>'
                    if med["otc"] else
                    '<span style="background:#FFF3CD;color:#856404;font-size:10px;font-weight:600;'
                    'padding:3px 10px;border-radius:12px;">Prescription Required</span>'
                )
                st.markdown(f"""
<div style="background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;margin-bottom:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.03);">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
    <div>
      <div style="font-size:15px;font-weight:700;color:#1a1a1a;">{med['name']}</div>
      <div style="font-size:11px;color:#999;margin-top:2px;">{med['type']}</div>
    </div>
    {otc_badge}
  </div>
  <div style="background:#f9f9f9;border-radius:8px;padding:10px 12px;margin-top:10px;">
    <div style="font-size:11px;color:#888;font-weight:500;">📋 Dosage</div>
    <div style="font-size:12px;color:#444;margin-top:2px;">{med['dosage']}</div>
  </div>
</div>
""", unsafe_allow_html=True)
                if st.button(f"➕ Add {med['name']} to My List", key=f"add_{med['name']}", use_container_width=True):
                    if med['name'] not in st.session_state.my_medicine_list:
                        st.session_state.my_medicine_list.append(med['name'])
                        st.success(f"Added {med['name']} to your list!")
                        time.sleep(0.5)
                        st.rerun()

            # Disclaimer
            st.markdown("""
<div style="background:#FFF9E6;border:1px solid #F7DC6F;border-radius:10px;padding:12px 14px;margin-top:8px;">
  <div style="font-size:11px;color:#856404;">
    ⚠️ <b>Disclaimer:</b> Always consult a licensed physician or pharmacist before taking any medication.
    This information is for educational purposes only and not a substitute for professional medical advice.
  </div>
</div>
""", unsafe_allow_html=True)

            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🥗  Get Diet Plan Too", use_container_width=True, key="med_goto_diet"):
                    st.session_state.page = "diet"
                    st.rerun()
            with c2:
                if st.button("📥  Download Report", use_container_width=True, key="med_goto_report"):
                    st.session_state.page = "report"
                    st.rerun()

        else:
            st.markdown("""
<div style="background:#f9f9f9;border:1px dashed #ddd;border-radius:16px;
            padding:48px 24px;text-align:center;">
  <div style="font-size:48px;margin-bottom:16px;">💊</div>
  <div style="font-size:15px;font-weight:600;color:#888;margin-bottom:8px;">No Condition Selected</div>
  <div style="font-size:12px;color:#bbb;line-height:1.7;">
    Choose a condition from the left panel<br>to view recommended medicines.
  </div>
</div>
""", unsafe_allow_html=True)