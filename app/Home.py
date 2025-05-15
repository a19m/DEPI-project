import streamlit as st
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler

# Page settings
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("📉 Customer Churn Prediction")
st.markdown("Will this customer leave the company? Let's find out!")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_churn_data.csv")

df = load_data()

# Load model
model = pickle.load(open("model_with_pip.pkl", "rb"))


# Sidebar input for customer details
st.sidebar.header("Enter Customer Details")

# Select input fields
gender = st.sidebar.selectbox("Gender", df["gender"].unique())
senior = st.sidebar.selectbox("Senior Citizen", df["SeniorCitizen"].unique())
partner = st.sidebar.selectbox("Partner", df["Partner"].unique())
dependents = st.sidebar.selectbox("Dependents", df["Dependents"].unique())
tenure = st.sidebar.slider("Tenure (Months)", 0, int(df["tenure"].max()), 12)
# Phone Service
phone_service = st.sidebar.selectbox("Phone Service", df["PhoneService"].unique())

# Multiple Lines
if phone_service == "No":
    multiple_lines = "No phone service"
    st.sidebar.selectbox("Multiple Lines", [multiple_lines], disabled=True)
else:
    filtered_multiple_lines = df["MultipleLines"].unique()
    filtered_multiple_lines = [opt for opt in filtered_multiple_lines if opt != "No phone service"]
    multiple_lines = st.sidebar.selectbox("Multiple Lines", filtered_multiple_lines)

# Internet Service
internet_service = st.sidebar.selectbox("Internet Service", df["InternetService"].unique())

# Internet-dependent features
if internet_service == "No":
    # Auto-set all to 'No internet service' and disable them
    online_security = "No internet service"
    online_backup = "No internet service"
    device_protection = "No internet service"
    tech_support = "No internet service"
    streaming_tv = "No internet service"
    streaming_movies = "No internet service"

    st.sidebar.selectbox("Online Security", [online_security], disabled=True)
    st.sidebar.selectbox("Online Backup", [online_backup], disabled=True)
    st.sidebar.selectbox("Device Protection", [device_protection], disabled=True)
    st.sidebar.selectbox("Tech Support", [tech_support], disabled=True)
    st.sidebar.selectbox("Streaming TV", [streaming_tv], disabled=True)
    st.sidebar.selectbox("Streaming Movies", [streaming_movies], disabled=True)

else:
    # Filter out 'No internet service'
    def clean_options(column):
        return [opt for opt in df[column].unique() if opt != "No internet service"]

    online_security = st.sidebar.selectbox("Online Security", clean_options("OnlineSecurity"))
    online_backup = st.sidebar.selectbox("Online Backup", clean_options("OnlineBackup"))
    device_protection = st.sidebar.selectbox("Device Protection", clean_options("DeviceProtection"))
    tech_support = st.sidebar.selectbox("Tech Support", clean_options("TechSupport"))
    streaming_tv = st.sidebar.selectbox("Streaming TV", clean_options("StreamingTV"))
    streaming_movies = st.sidebar.selectbox("Streaming Movies", clean_options("StreamingMovies"))

contract = st.sidebar.selectbox("Contract Type", df["Contract"].unique())
paperless_billing = st.sidebar.selectbox("Paperless Billing", df["PaperlessBilling"].unique())
payment_method = st.sidebar.selectbox("Payment Method", df["PaymentMethod"].unique())
monthly_charges = st.sidebar.slider("Monthly Charges", float(df["MonthlyCharges"].min()), float(df["MonthlyCharges"].max()), 70.0)
total_charges = st.sidebar.slider("Total Charges", float(df["TotalCharges"].min()), float(df["TotalCharges"].max()), 1500.0)

# Create feature DataFrame
features = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})


# Show predict button
st.markdown("---")
if st.button("🔮 Predict Churn"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1] * 100
    if prediction == 1:
        st.error(f"⚠️ This customer is likely to **leave**. (Confidence: {probability:.2f}%)")
    else:
        st.success(f"✅ This customer is likely to **stay**. (Confidence: {100-probability:.2f}%)")
