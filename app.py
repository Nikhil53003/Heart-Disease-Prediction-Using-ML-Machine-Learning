import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓", layout="centered")

# Light background CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f4f8;
        background-image: linear-gradient(to bottom right, #f0f4f8, #ffffff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Simulated user credentials
USER_CREDENTIALS = {
    "admin": "1234",
    "user": "pass"
}

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

def main_app():
    st.title("💓 Heart Disease Prediction")
    st.markdown("Predict the likelihood of heart disease using your medical data.")

    model = joblib.load("model_joblib_heart")

    st.sidebar.header("📝 Input Your Medical Info")

    age = st.sidebar.number_input("👤 Age", min_value=1, max_value=120, value=45)
    sex = st.sidebar.radio("⚧️ Sex", ["Male", "Female"])
    cp = st.sidebar.selectbox("💥 Chest Pain Type", [
        "0: Typical angina",
        "1: Atypical angina",
        "2: Non-anginal pain",
        "3: Asymptomatic"
    ])
    trestbps = st.sidebar.slider("🩺 Resting BP (mm Hg)", 80, 200, 130)
    chol = st.sidebar.slider("🧪 Cholesterol (mg/dl)", 100, 600, 250)
    fbs = st.sidebar.radio("🍬 Fasting Blood Sugar > 120?", ["No", "Yes"])
    restecg = st.sidebar.selectbox("📉 Resting ECG", [
        "0: Normal",
        "1: ST-T Abnormality",
        "2: Left Ventricular Hypertrophy"
    ])
    thalach = st.sidebar.slider("❤️ Max Heart Rate", 60, 220, 150)
    exang = st.sidebar.radio("🏃‍♂️ Exercise Induced Angina?", ["No", "Yes"])
    oldpeak = st.sidebar.slider("📉 ST Depression (Oldpeak)", 0.0, 6.0, 1.0, step=0.1)
    slope = st.sidebar.selectbox("📈 Slope of ST Segment", [
        "0: Upsloping",
        "1: Flat",
        "2: Downsloping"
    ])
    ca = st.sidebar.selectbox("🩻 Major Vessels Colored (0–3)", [0, 1, 2, 3])
    thal = st.sidebar.selectbox("🧬 Thalassemia", [
        "1: Normal",
        "2: Fixed defect",
        "3: Reversible defect"
    ])

    input_data = pd.DataFrame([[age,
                                1 if sex == "Male" else 0,
                                int(cp[0]),
                                trestbps,
                                chol,
                                1 if fbs == "Yes" else 0,
                                int(restecg[0]),
                                thalach,
                                1 if exang == "Yes" else 0,
                                oldpeak,
                                int(slope[0]),
                                ca,
                                int(thal[0])
                                ]])

    with st.expander("📁 View Previous Records"):
        if os.path.exists("records.csv"):
            history_df = pd.read_csv("records.csv")
            user = st.session_state.get("username", "Unknown")
            user_df = history_df[history_df["User"] == user]
            st.dataframe(user_df)
        else:
            st.info("No records found yet.")

    if st.button("🔍 Predict Now"):
        prediction = model.predict(input_data)
        result = "High Risk" if prediction[0] == 1 else "Low Risk"

        if result == "High Risk":
            st.error("⚠️ **High Risk**: The model predicts that you **may have heart disease**. Please consult a doctor.")
        else:
            st.success("✅ **Low Risk**: You are **unlikely to have heart disease**. Keep up the healthy lifestyle! 😊")

        input_data["Result"] = result
        input_data["User"] = st.session_state.get("username", "Unknown")

        if not os.path.exists("records.csv"):
            input_data.to_csv("records.csv", index=False)
        else:
            input_data.to_csv("records.csv", mode="a", header=False, index=False)

        st.success("📝 Prediction record saved!")

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")

# Run login or main app
if not st.session_state.get("logged_in", False):
    login()
else:
    main_app()