import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Visual Analysis", layout="wide")
st.title("📊 Customer Churn - Data Visualizations")

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_churn_data.csv")

df = load_data()

st.markdown("### 🔍 General Overview")
st.dataframe(df.describe(include="object"))
st.dataframe(df.describe(include="number").drop(columns=["Churn_num"]))

# Churn Distribution
st.markdown("### 📈 Churn Distribution")
fig1 = px.histogram(df, x="Churn", title="Churn Distribution", width=600, height=400)
st.plotly_chart(fig1)

# Senior Citizen vs Churn
st.markdown("### 👵 Senior Citizens vs Churn")
fig2 = px.histogram(df, x="SeniorCitizen", color="Churn", barmode="group",
                    title="Senior Citizen Status by Churn", width=600, height=400)
st.plotly_chart(fig2)

# Monthly Charges
st.markdown("### 💳 Monthly Charges Distribution")
fig3 = px.histogram(df, x="MonthlyCharges", nbins=30, marginal="box", 
                    title="Monthly Charges Distribution", width=600, height=400)
st.plotly_chart(fig3)

# Churn by Contract Type
st.markdown("### 📉 Churn Rate by Contract Type")
fig4 = px.histogram(df, x="Contract", color="Churn", barmode="group",
                    title="Churn by Contract Type", width=600, height=400)
st.plotly_chart(fig4)

# Custom Feature Explorer
st.markdown("### 🔬 Custom Feature Exploration")
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
selected_feature = st.selectbox("Choose a categorical feature", categorical_cols)

fig5 = px.histogram(df, x=selected_feature, color="Churn", barmode="group",
                    title=f"{selected_feature} vs Churn", width=700, height=400)
fig5.update_layout(xaxis_title=selected_feature, yaxis_title="Count")
st.plotly_chart(fig5)
