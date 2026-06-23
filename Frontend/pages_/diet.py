import streamlit as st
import time

# ── Sample Data (backend teammate replaces this with real DB / model) ────────
DIET_DB = {
    "Fungal Infection": {
        "icon": "🍄",
        "eat": ["Garlic & onions (antifungal)", "Yogurt with probiotics", "Leafy greens", "Coconut oil"],
        "avoid": ["Sugar & sweets", "Refined carbs", "Alcohol", "Processed foods"],
        "tip": "Keep your diet low in sugar — fungi thrive on sugar.",
    },
    "Common Cold": {
        "icon": "🤧",
        "eat": ["Citrus fruits (Vitamin C)", "Warm soups & broths", "Ginger tea", "Honey"],
        "avoid": ["Dairy products", "Cold beverages", "Fried foods", "Sugary drinks"],
        "tip": "Stay hydrated with warm fluids to ease congestion.",
    },
    "Diabetes": {
        "icon": "💉",
        "eat": ["Whole grains", "Leafy green vegetables", "Lean proteins", "Nuts & seeds"],
        "avoid": ["Sugary drinks", "White bread & rice", "Fried foods", "Processed snacks"],
        "tip": "Eat smaller, frequent meals to keep blood sugar stable.",
    },
    "Hypertension": {
        "icon": "❤️",
        "eat": ["Bananas (potassium)", "Oats", "Beetroot juice", "Leafy greens"],
        "avoid": ["Salt & sodium", "Processed meats", "Canned foods", "Caffeine (excess)"],
        "tip": "Follow the DASH diet — reduce sodium to under 1500mg/day.",
    },
    "Migraine": {
        "icon": "🧠",
        "eat": ["Magnesium-rich foods (spinach)", "Ginger", "Water-rich fruits", "Whole grains"],
        "avoid": ["Caffeine (excess)", "Aged cheese", "Processed meats", "Alcohol"],
        "tip": "Keep blood sugar steady — don't skip meals.",
    },
    "Typhoid": {
        "icon": "🤒",
        "eat": ["Soft khichdi", "Boiled vegetables", "Bananas", "ORS / coconut water"],
        "avoid": ["Spicy food", "Raw vegetables", "Street food", "Caffeinated drinks"],
        "tip": "Stick to a soft, bland diet until fully recovered.",
    },
    "Malaria": {
        "icon": "🦟",
        "eat": ["Fresh fruit juices", "Soups", "Papaya leaf extract", "Iron-rich foods"],
        "avoid": ["Fatty foods", "Caffeine", "Alcohol", "Processed sugar"],
        "tip": "Focus on fluids and iron-rich foods to combat fatigue.",
    },
    "Dengue": {
        "icon": "🌡️",
        "eat": ["Papaya leaf juice", "Pomegranate", "Coconut water", "Vegetable soups"],
        "avoid": ["Oily food", "Spicy food", "Carbonated drinks", "Caffeine"],
        "tip": "Increase fluid intake to prevent dehydration and support platelets.",
    },
    "Jaundice": {
        "icon": "😷",
        "eat": ["Sugarcane juice", "Fresh fruits", "Boiled vegetables", "Coconut water"],
        "avoid": ["Fatty/oily food", "Alcohol", "Processed food", "Excess protein"],
        "tip": "A low-fat diet helps reduce the load on your liver.",
    },
    "Pneumonia": {
        "icon": "🫁",
        "eat": ["Warm soups", "Vitamin C fruits", "Garlic & ginger", "Protein-rich foods"],
        "avoid": ["Dairy (excess mucus)", "Fried food", "Sugary snacks", "Alcohol"],
        "tip": "Stay hydrated and eat protein to support immune recovery.",
    },
}

GOALS = ["⚖️ Weight Management", "💪 Muscle Gain", "🥗 General Wellness", "🩺 Condition-Specific"]


def show():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.diet-card {
    animation: fadeInUp 0.4s ease;
}

@keyframes pulse {
    0%   { transform: scale(1); }
    50%  { transform: scale(1.04); }
    100% { transform: scale(1); }
}
.pulse-icon {
    animation: pulse 2s ease-in-out infinite;
    display: inline-block;
}

.food-pill {
    display: inline-flex;
    align-items: center;
    background: #E1F5EE;
    color: #0B7285;
    border-radius: 20px;
    padding: 7px 14px;
    font-size: 12px;
    font-weight: 500;
    margin: 4px 6px 4px 0;
    transition: transform 0.15s ease;
}
.food-pill:hover { transform: translateY(-2px); }

.avoid-pill {
    display: inline-flex;
    align-items: center;
    background: #FDEDED;
    color: #C0392B;
    border-radius: 20px;
    padding: 7px 14px;
    font-size: 12px;
    font-weight: 500;
    margin: 4px 6px 4px 0;
    transition: transform 0.15s ease;
}
.avoid-pill:hover { transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

    if "diet_condition" not in st.session_state:
        st.session_state.diet_condition = None
    if "diet_goal" not in st.session_state:
        st.session_state.diet_goal = None

    # Auto-fill from prediction
    if st.session_state.get("prediction_result") and not st.session_state.diet_condition:
        if st.session_state.prediction_result in DIET_DB:
            st.session_state.diet_condition = st.session_state.prediction_result

    # ── HERO HEADER (same teal palette as login/signup) ──────────────────
    st.markdown("""
<div style="background:linear-gradient(135deg,#0B7285 0%,#1aabbd 100%);
            border-radius:16px;padding:32px 36px;margin-bottom:24px;
            display:flex;align-items:center;gap:20px;position:relative;overflow:hidden;">
  <div style="position:absolute;top:-30px;right:-30px;width:140px;height:140px;
              background:rgba(255,255,255,0.06);border-radius:50%;"></div>
  <div class="pulse-icon" style="font-size:48px;">🥗</div>
  <div>
    <div style="font-size:22px;font-weight:700;color:#fff;">Diet Recommendation</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-top:4px;">
      Personalised nutrition plans to support your recovery and wellness
    </div>
  </div>
  <div style="margin-left:auto;background:rgba(255,255,255,0.15);border-radius:12px;padding:12px 20px;text-align:center;">
    <div style="font-size:22px;font-weight:700;color:#fff;">10+</div>
    <div style="font-size:10px;color:rgba(255,255,255,0.6);">Diet plans</div>
  </div>
</div>
""", unsafe_allow_html=True)

    if st.session_state.get("prediction_result") and st.session_state.diet_condition == st.session_state.prediction_result:
        st.markdown(
            f'<div style="background:#E1F5EE;border:1px solid #b2dfdb;border-radius:10px;'
            f'padding:10px 16px;margin-bottom:18px;font-size:12px;color:#0B7285;">'
            f'✨ Auto-filled from your recent prediction: <b>{st.session_state.prediction_result}</b></div>',
            unsafe_allow_html=True,
        )

    # ── GOAL SELECTOR ──────────────────────────────────────────────────────
    st.markdown('<div style="font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:10px;">🎯 What\'s your goal?</div>', unsafe_allow_html=True)
    goal_cols = st.columns(4)
    for col, goal in zip(goal_cols, GOALS):
        with col:
            is_active = st.session_state.diet_goal == goal
            bg = "#0B7285" if is_active else "#fff"
            txt_color = "#fff" if is_active else "#444"
            border = "#0B7285" if is_active else "#eee"
            st.markdown(
                f'<div style="background:{bg};border:1.5px solid {border};border-radius:12px;'
                f'padding:12px 8px;text-align:center;margin-bottom:6px;transition:all 0.2s;">'
                f'<span style="font-size:12px;font-weight:600;color:{txt_color};">{goal}</span></div>',
                unsafe_allow_html=True,
            )
            if st.button("Select", key=f"goal_{goal}", use_container_width=True):
                st.session_state.diet_goal = goal
                st.rerun()

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 1.4], gap="large")

    # ── LEFT: CONDITION SELECTOR ──────────────────────────────────────────
    with left_col:
        st.markdown('<div style="font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:12px;">🩺 Select a Condition</div>', unsafe_allow_html=True)

        conditions = list(DIET_DB.keys())
        for cond in conditions:
            data = DIET_DB[cond]
            is_selected = st.session_state.diet_condition == cond
            border = "2px solid #0B7285" if is_selected else "1px solid #eee"
            bg = "#E1F5EE" if is_selected else "#fff"

            st.markdown(
                f'<div style="background:{bg};border:{border};border-radius:12px;'
                f'padding:10px 14px;margin-bottom:6px;display:flex;align-items:center;gap:10px;">'
                f'<span style="font-size:20px;">{data["icon"]}</span>'
                f'<span style="font-size:13px;font-weight:600;color:#1a1a1a;">{cond}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if st.button("View Plan" if not is_selected else "✓ Viewing", key=f"diet_cond_{cond}", use_container_width=True):
                st.session_state.diet_condition = cond
                st.rerun()

    # ── RIGHT: DIET PLAN DETAILS ───────────────────────────────────────────
    with right_col:
        if st.session_state.diet_condition:
            cond = st.session_state.diet_condition
            data = DIET_DB[cond]

            st.markdown(f"""
<div class="diet-card" style="display:flex;align-items:center;gap:14px;margin-bottom:18px;">
  <div style="font-size:36px;">{data['icon']}</div>
  <div>
    <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;">Diet Plan for</div>
    <div style="font-size:20px;font-weight:700;color:#1a1a1a;">{cond}</div>
  </div>
</div>
""", unsafe_allow_html=True)

            # Tip banner
            st.markdown(f"""
<div class="diet-card" style="background:linear-gradient(135deg,#0B7285,#1aabbd);border-radius:12px;
            padding:14px 18px;margin-bottom:18px;display:flex;align-items:center;gap:12px;">
  <span style="font-size:22px;">💡</span>
  <span style="font-size:12.5px;color:#fff;line-height:1.5;">{data['tip']}</span>
</div>
""", unsafe_allow_html=True)

            # Foods to eat
            eat_pills = "".join(f'<span class="food-pill">✅ {item}</span>' for item in data["eat"])
            st.markdown(f"""
<div class="diet-card" style="background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;margin-bottom:14px;
            box-shadow:0 2px 8px rgba(0,0,0,0.03);">
  <div style="font-size:13px;font-weight:700;color:#0B7285;margin-bottom:12px;">🥦 Foods to Include</div>
  <div>{eat_pills}</div>
</div>
""", unsafe_allow_html=True)

            # Foods to avoid
            avoid_pills = "".join(f'<span class="avoid-pill">🚫 {item}</span>' for item in data["avoid"])
            st.markdown(f"""
<div class="diet-card" style="background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;margin-bottom:14px;
            box-shadow:0 2px 8px rgba(0,0,0,0.03);">
  <div style="font-size:13px;font-weight:700;color:#C0392B;margin-bottom:12px;">⛔ Foods to Avoid</div>
  <div>{avoid_pills}</div>
</div>
""", unsafe_allow_html=True)

            # Sample meal plan progress bars (illustrative)
            st.markdown('<div class="diet-card" style="background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,0.03);">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:13px;font-weight:700;color:#1a1a1a;margin-bottom:14px;">📅 Suggested Daily Balance</div>', unsafe_allow_html=True)

            macros = [("Vegetables & Fruits", 40, "#27AE60"), ("Whole Grains", 30, "#0B7285"), ("Protein", 20, "#534AB7"), ("Healthy Fats", 10, "#F39C12")]
            for label, pct, color in macros:
                st.markdown(f"""
<div style="margin-bottom:10px;">
  <div style="display:flex;justify-content:space-between;font-size:11px;color:#666;margin-bottom:4px;">
    <span>{label}</span><span style="font-weight:600;color:{color};">{pct}%</span>
  </div>
  <div style="background:#f0f0f0;border-radius:6px;height:7px;">
    <div style="background:{color};width:{pct}%;height:7px;border-radius:6px;transition:width 0.6s ease;"></div>
  </div>
</div>
""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Disclaimer
            st.markdown("""
<div style="background:#FFF9E6;border:1px solid #F7DC6F;border-radius:10px;padding:12px 14px;">
  <div style="font-size:11px;color:#856404;">
    ⚠️ <b>Disclaimer:</b> This diet plan is a general guideline. Please consult a registered dietitian
    or your doctor for a plan tailored to your specific medical needs.
  </div>
</div>
""", unsafe_allow_html=True)

            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("💊  View Medicines", use_container_width=True, key="diet_goto_med"):
                    st.session_state.page = "medicine"
                    st.rerun()
            with c2:
                if st.button("📥  Download Report", use_container_width=True, key="diet_goto_report"):
                    st.session_state.page = "report"
                    st.rerun()

        else:
            st.markdown("""
<div style="background:#f9f9f9;border:1px dashed #ddd;border-radius:16px;
            padding:48px 24px;text-align:center;">
  <div style="font-size:48px;margin-bottom:16px;" class="pulse-icon">🥗</div>
  <div style="font-size:15px;font-weight:600;color:#888;margin-bottom:8px;">No Condition Selected</div>
  <div style="font-size:12px;color:#bbb;line-height:1.7;">
    Choose a condition from the left panel<br>to view your personalised diet plan.
  </div>
</div>
""", unsafe_allow_html=True)