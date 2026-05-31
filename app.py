import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. Page Config
st.set_page_config(
    page_title="DuoDevotion AI", 
    page_icon="💖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for "App-like" feel
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 🌟 NEW STAGE: Load the real trained models from Colab
@st.cache_resource
def load_ml_models():
    try:
        # Make sure these files match what you downloaded from your sidebar exactly!
        match_model = joblib.load('automl_match_model.pkl')
        risk_model = joblib.load('automl_risk_model.pkl')
        return match_model, risk_model
    except Exception as e:
        st.error(f"Error loading model files: {e}. Ensure '.pkl' files are in the same folder as app.py")
        return None, None

automl_match, automl_risk = load_ml_models()

# 3. Sidebar - Settings & Model Selection
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2589/2589175.png", width=100)
    st.title("Settings")
    
    st.subheader("Model Configuration")
    # Updated to display the active operational AutoML model
    model_choice = st.selectbox(
        "Select Prediction Model", 
        ["FLAML AutoML (XGBoost Benchmark)", "Static Fallback Engine"],
        help="Currently utilizing the optimized model pipeline trained via Google Colab."
    )
    
    st.divider()
    st.info("DuoDevotion v1.0 - Active ML Build")

# 4. Main App Tabs
tab1, tab2, tab3 = st.tabs(["✨ Prediction Tool", "📖 Methodology", "👩‍💻 The Team"])

with tab1:
    st.title("💖 DuoDevotion AI")
    st.write("Determine the heartbeat of your connection.")
    
    # Input Area
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 User 1 (Applicant)")
        u1_usage = st.select_slider("App Engagement Level", options=list(range(1, 11)), value=5, key="u1_s1")
        u1_pics = st.number_input("Profile Pictures", 1, 15, 3, key="u1_n1")
        u1_bio = st.slider("Bio Word Count", 0, 500, 50, key="u1_s2")
        
        # Encodings map category strings directly to numerical input metrics
        u1_outcome_str = st.selectbox("Last Match Experience", ["None", "Successful Date", "Ghosted"], key="u1_b1")
        u1_outcome = 0 if u1_outcome_str == "None" else (1 if u1_outcome_str == "Successful Date" else 2)

    with col2:
        st.markdown("### 👤 User 2 (Partner)")
        u2_income_str = st.selectbox("Income Bracket", ["Low", "Medium", "High", "Very High"], key="u2_b1")
        u2_income = 0 if u2_income_str == "Low" else (1 if u2_income_str == "Medium" else (2 if u2_income_str == "High" else 3))
        
        u2_usage_min = st.number_input("Daily Active Minutes", 0, 1440, 60, key="u2_n1")
        u2_swipe = st.slider("Right Swipe Ratio", 0.0, 1.0, 0.5, key="u2_s1")
        
        u2_outcome_str = st.selectbox("Last Match Experience", ["None", "Successful Date", "Ghosted"], key="u2_b2")
        u2_outcome = 0 if u2_outcome_str == "None" else (1 if u2_outcome_str == "Successful Date" else 2)

    st.divider()

    # The Analysis Button
    if st.button("🚀 Run DuoDevotion Analysis"):
        if automl_match is not None and automl_risk is not None:
            with st.spinner('AI is calculating real pipeline chemistry matrices...'):
                
                # ⚠️ CRITICAL STEP: Construct features in the precise column order your X_train used.
                # Adjust the list array order below to match your exact 8 features column placement!
                feature_array = np.array([[
                    u1_usage, u1_pics, u1_bio, u1_outcome,
                    u2_income, u2_usage_min, u2_swipe, u2_outcome
                ]])
                
                # Predict probabilities ([0][1] pulls the probability score of class 1)
                match_proba = automl_match.predict_proba(feature_array)[0][1]
                risk_proba = automl_risk.predict_proba(feature_array)[0][1]
                
                # Scale probabilities elegantly to percentages
                score_pct = int(match_proba * 100)
                risk_pct = int(risk_proba * 100)
                
                st.balloons()
                
                # Results Display
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.metric("Compatibility Score", f"{score_pct}%")
                with res_col2:
                    st.metric("Ghosting Risk", f"{risk_pct}%", delta="- Low" if risk_pct < 35 else "+ High", delta_color="inverse")
                
                # Live AI Evaluation feedback
                st.markdown("---")
                st.markdown("### 📝 AI Advisory Recommendation")
                if score_pct >= 50:
                    st.success(f"**Analysis Result:** Based on {model_choice}, your profiles show strong baseline correlation with an active verification score.")
                else:
                    st.warning(f"**Analysis Result:** Based on {model_choice}, compatibility tracking scales low. Divergence found in relative application interaction parameters.")
                st.info("💡 **Pro-Tip:** Adjusting engagement trends or enhancing profile metrics like bio structure maximizes cross-pipeline predictability.")
        else:
            st.error("Model engines are uninitialized. Check local model file workspace properties.")

with tab2:
    st.header("How it Works")
    st.write("""
    Our engine uses 8 distinct behavioral features to predict relationship outcomes. 
    By analyzing patterns in app usage, profile presentation, and historical success, 
    we provide a data-driven look at modern romance.
    """)
    st.image("https://img.freepik.com/free-vector/dating-app-concept-illustration_114360-1044.jpg", width=400)

with tab3:
    st.header("The DuoDevotion Team")
    st.write("Building the future of digital connection.")
    
    # Team display
    tcol1, tcol2, tcol3 = st.columns(3)
    with tcol1:
        st.subheader("XXX")
        st.caption("Dashboard & Lead")
    with tcol2:
        st.subheader("XXX")
        st.caption("Machine Learning")
    with tcol3:
        st.subheader("XXX")
        st.caption("Data Analyst")