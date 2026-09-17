import streamlit as st
import requests
import os

# ---- Config ----
API_URL = os.getenv("API_URL","http://127.0.0.1:8000/predict")  # change if your FastAPI runs elsewhere

st.set_page_config(page_title="Black Friday Purchase Predictor", page_icon="🛍️")
st.title("🛍️ Black Friday Purchase Predictor")
st.write("Enter customer details to predict purchase amount.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", options=["F", "M"])
        age = st.number_input("Age", min_value=0, max_value=120, value=25, step=1)
        occupation = st.text_input("Occupation", value="Architect")
        city_category = st.selectbox("City Category", options=["pune", "mumbai", "nagpur"])

    with col2:
        stay_years = st.number_input(
            "Stay in Current City (Years)", min_value=0, max_value=4, value=1, step=1
        )
        marital_status = st.selectbox(
            "Marital Status", options=[0, 1], format_func=lambda x: "Single" if x == 0 else "Married"
        )
        product_cat_1 = st.number_input("Product Category 1", min_value=0, value=1, step=1)
        product_cat_2 = st.number_input("Product Category 2", min_value=0, value=0, step=1)
        product_cat_3 = st.number_input("Product Category 3", min_value=0, value=0, step=1)

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "City_Category": city_category,
        "Stay_In_Current_City_Years": stay_years,
        "Marital_Status": marital_status,
        "Product_Category_1": product_cat_1,
        "Product_Category_2": product_cat_2,
        "Product_Category_3": product_cat_3,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result}")
        else:
            st.error(f"API returned {response.status_code}: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the API. Make sure your FastAPI server "
            f"is running at {API_URL.replace('/predict', '')}"
        )
    except requests.exceptions.Timeout:
        st.error("Request timed out. Check if the FastAPI server is responsive.")