import streamlit as st
import random

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

# 3. Sidebar - Settings & Model Selection
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2589/2589175.png", width=100)
    st.title("Settings")
    
    st.subheader("Model Configuration")
    # Placeholder for Wei Xin's 5 models
    model_choice = st.selectbox(
        "Select Prediction Model", 
        ["[Empty] Random Forest", "[Empty] Logistic Regression", "[Empty] SVM", "[Empty] Neural Network", "[Empty] XGBoost"],
        help="Once the models are trained, you can switch between them here."
    )
    
    st.divider()
    st.info("DuoDevotion v1.0 - Week 1 Build")

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
        u1_outcome = st.selectbox("Last Match Experience", ["None", "Successful Date", "Ghosted"], key="u1_b1")

    with col2:
        st.markdown("### 👤 User 2 (Partner)")
        u2_income = st.selectbox("Income Bracket", ["Low", "Medium", "High", "Very High"], key="u2_b1")
        u2_usage_min = st.number_input("Daily Active Minutes", 0, 1440, 60, key="u2_n1")
        u2_swipe = st.slider("Right Swipe Ratio", 0.0, 1.0, 0.5, key="u2_s1")
        u2_outcome = st.selectbox("Last Match Experience", ["None", "Successful Date", "Ghosted"], key="u2_b2")

    st.divider()

    # The Analysis Button
    if st.button("🚀 Run DuoDevotion Analysis"):
        # Simulated "Thinking" process
        with st.spinner('AI is analyzing the chemistry...'):
            import time
            time.sleep(1) # Makes the app feel like it's calculating
            
            score = random.randint(65, 98)
            risk = random.randint(2, 35)
            
            st.balloons()
            
            # Results Display
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric("Compatibility Score", f"{score}%")
            with res_col2:
                st.metric("Ghosting Risk", f"{risk}%", delta="- Low" if risk < 20 else "+ High", delta_color="inverse")
            
            # AI Advisory (Phase 2 Preview)
            st.markdown("---")
            st.markdown("### 📝 AI Advisory Recommendation")
            st.success(f"**Analysis Result:** Based on {model_choice}, the duo shows strong alignment. User 2's engagement matches User 1's profile depth.")
            st.info("💡 **Pro-Tip:** Try sending a message about a specific detail in their bio to reduce ghosting risk by an estimated 12%.")

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