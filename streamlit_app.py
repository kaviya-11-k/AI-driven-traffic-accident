import streamlit as st
import numpy as np
import pandas as pd
import random

# App Title
st.title("🚦 AI-Powered Traffic Accident Prediction")
st.subheader("Predict accident risk based on location, weather, and time inputs")

# Sidebar Inputs
st.sidebar.header("Enter Traffic Details")

location = st.sidebar.selectbox("Location", ["Downtown", "Suburb", "Highway", "Rural"])
time_of_day = st.sidebar.slider("Time of Day", 0, 23, 17)
weather = st.sidebar.selectbox("Weather", ["Clear", "Rainy", "Foggy", "Snowy"])
vehicle_speed = st.sidebar.number_input("Vehicle Speed (km/h)", min_value=0, max_value=200, value=50)
road_type = st.sidebar.selectbox("Road Type", ["Urban", "Highway", "Rural"])
day_of_week = st.sidebar.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# Simulate a prediction (replace this with your actual ML model)
risk_score = random.uniform(0, 1)
risk_level = "Low"
if risk_score > 0.7:
    risk_level = "High"
elif risk_score > 0.4:
    risk_level = "Moderate"

# Display Prediction Output
st.markdown("### 🧠 Prediction Results")
st.metric(label="Accident Risk Level", value=risk_level)
st.metric(label="Probability", value=f"{risk_score*100:.2f}%")

# Recommendation
if risk_level == "High":
    st.warning("⚠️ High Risk: Reduce speed and stay alert.")
elif risk_level == "Moderate":
    st.info("⚠️ Moderate Risk: Drive carefully.")
else:
    st.success("✅ Low Risk: Normal driving conditions.")

# Visualization Placeholder
st.markdown("### 📊 Accident Data Visualization (Placeholder)")
st.image("https://via.placeholder.com/600x300.png?text=Heatmap+or+Accident+Trends")

# Footer
st.markdown("---")
st.caption("Model demo for road safety awareness. Replace with actual model for production.")
