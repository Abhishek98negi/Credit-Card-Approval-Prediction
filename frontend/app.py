import os
import requests
import streamlit as st


# API_URL = "http://127.0.0.1:8000/predict-credit-card-approval"

# Defaults to localhost for local testing, uses Render URL in production
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Credit Card approval prediction",
    page_icon="💳",
    layout="centered"
)

st.title("💳Credit Card Approval Prediction")

st.subheader("Enter Customer's details and click **Predict**")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender", 
        options=["M", "F"], 
        format_func=lambda x: "Male" if x == "M" else "Female"
    )
    car_owner = st.selectbox(
        "Car Owner", 
        options=["Y", "N"], 
        format_func=lambda x: "Yes" if x == "Y" else "No"
    )
    property_owner = st.selectbox(
        "Property Owner", 
        options=["Y", "N"], 
        format_func=lambda x: "Yes" if x == "Y" else "No"
    )
    annual_income = st.number_input(
        "Annual Income",
        min_value=0,
        max_value=1000000000,
        value=None,
        placeholder="Enter annual income"
    )
    education = st.selectbox("Education Level", ["Higher education", "Secondary / secondary special", "Incomplete higher",
                                                  "Lower secondary", "Academic degree"])

with col2:
    type_income = st.selectbox("Type of Income", ["Working", "Commercial associate", "State servant", "Pensioner", "Unemployed",
                                                   "Student"])
    marital_status = st.selectbox("Marital Status", ["Married", "Single / not married", "Civil marriage", "Separated", "Widow"])

    housing_type = st.selectbox("Housing Type", ["House / apartment", "With parents", "Municipal apartment", "Rented apartment",
                                                  "Office apartment", "Co-op apartment"])
    work_phone= st.selectbox(
        "work phone", 
        options=[0, 1], 
        format_func=lambda x: "Yes" if x == 1 else "No"
    )
    phone= st.selectbox(
        "landline phone", 
        options=[0, 1], 
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with col3:
    email_id= st.selectbox(
            "email id", 
            options=[0, 1], 
            format_func=lambda x: "Yes" if x == 1 else "No"
        )
    type_occupation = st.selectbox("Type of Occupation", ["Others", "Laborers", "Core staff", "Accountants", "Managers", "Drivers",
        "Sales staff", "High skill tech staff", "Medicine staff", "Cooking staff", "Security staff", "Cleaning staff", 
        "Private service staff", "Low-skill Laborers", "Waiters/barmen staff", "Secretaries", "Realty agents", "HR staff", "IT staff"])
    family_members = st.number_input("Number of Family Members", 0, 20, 2)
    age = st.number_input("Age", 18, 80, value=None,
            placeholder="Enter Your age")
    employment_years = st.number_input("Years of Employment", 0, 50, value=None,
            placeholder="Enter years of employment")


if st.button("🔍 Predict"):
    if annual_income is None:
        st.error("Please enter a valid annual income.")
    elif age is None or not isinstance(age, int):
        st.error("Please enter a valid age.")
    elif employment_years is None:
        st.error("Please enter a valid number of employment years.")
    elif employment_years > age - 18:
        st.error("Employment years cannot exceed the number of years since age 18.")
    else:

        input_data = {
            "GENDER": gender,
            "Car_Owner": car_owner,
            "Propert_Owner": property_owner,
            "Annual_income": annual_income,
            "Type_Income": type_income,
            "EDUCATION": education,
            "Marital_status": marital_status,
            "Housing_type": housing_type,
            "Work_Phone": work_phone,
            "Phone": phone,
            "EMAIL_ID": email_id,
            "Type_Occupation": type_occupation,
            "Family_Members": family_members,
            "Age": age,
            "Employment_years": employment_years
        }

        # response = requests.post(f"{BACKEND_URL}/predict-credit-card-approval", json=input_data)
        response = requests.post(BACKEND_URL, json=input_data)
        if response.status_code != 200:
            st.error("Something went wrong. Try again later...")
        
        else:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            st.divider()

            st.metric(
                label="Credit Card Approval Probability",
                value=f"{probability:.2f}"
            )

            if prediction == 1:
                st.error(f"⚠️Credit card will not be approved.")
            else:
                st.success(f"✅ Credit card will be approved.")

# streamlit run frontend/app.py