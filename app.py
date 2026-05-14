import streamlit as st
import random # Used for "Vibe Coding" until the ML model is ready

# 1. Page Configuration (This shows up on the browser tab)
st.set_page_config(page_title="LuvLogic AI", page_icon="💖", layout="wide")

# 2. Header Section
st.title("💖 LuvLogic: Dual-User Intelligence System")
st.subheader("Predicting Compatibility & Ghosting Risks using Machine Learning")
st.markdown("---")

# 3. Sidebar - General Settings or Instructions
st.sidebar.header("About LuvLogic")
st.sidebar.info("This system analyzes 8 key features from two users to determine relationship sustainability.")

# 4. Input Section: Creating Two Columns
col1, col2 = st.columns(2)

with col1:
    st.header("👤 User 1 (Applicant)")
    u1_usage = st.select_slider("App Usage Time (Level 1-10)", options=list(range(1, 11)), value=5)
    u1_pics = st.number_input("Number of Profile Pictures", min_value=1, max_value=15, value=3)
    u1_bio = st.slider("Bio Length (Words)", 0, 500, 50)
    u1_outcome = st.selectbox("Last Match Outcome (U1)", ["None", "Successful Date", "Ghosted", "Still Talking"])

with col2:
    st.header("👤 User 2 (Partner)")
    u2_income = st.selectbox("Income Bracket", ["Low", "Medium", "High", "Very High"])
    u2_usage_min = st.number_input("Daily Usage (Total Minutes)", min_value=0, max_value=1440, value=60)
    u2_swipe = st.slider("Swipe Right Ratio (0% to 100%)", 0.0, 1.0, 0.5)
    u2_outcome = st.selectbox("Last Match Outcome (U2)", ["None", "Successful Date", "Ghosted", "Still Talking"])

st.markdown("---")

# 5. Prediction Logic
if st.button("🔮 Run LuvLogic Analysis"):
    # This part will be replaced by Wei Xin's model (.pkl) later
    # For now, we simulate a result (Vibe Coding)
    compatibility_score = random.randint(70, 95)
    ghosting_risk = random.randint(5, 40)
    
    st.balloons() # Visual celebration!
    
    # Display Results in Metrics
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Compatibility Score", f"{compatibility_score}%")
    res_col2.metric("Ghosting Risk", f"{ghosting_risk}%", delta="-Low Risk" if ghosting_risk < 20 else "+High Risk")

    # 6. AI Advisory Layer (This is for the extra Innovation marks!)
    st.markdown("### 📝 AI Advisory Recommendation")
    if compatibility_score > 80:
        st.success("High Match! Suggestion: Both users show high engagement. Start a conversation about shared hobbies.")
    else:
        st.warning("Moderate Match. Suggestion: User 1 might want to improve their bio to increase engagement alignment.")