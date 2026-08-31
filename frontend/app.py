import os
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/predict-credit-card-approval"

st.set_page_config(
    page_title="Credit Card approval prediction",
    page_icon="💳",
    layout="centered"
)

st.title("💳Credit Card Approval Prediction")

st.subheader("Enter Customer's details and click **Predict**")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender (1 = Male, 0 = Female)", [0, 1])
    car_owner = st.selectbox("Car Owner (1 = Yes, 0 = No)", [0, 1])
    property_owner = st.selectbox("Property Owner (1 = Yes, 0 = No)", [0, 1])
    annual_income = st.number_input("Annual Income", 0, 1000000, 50000)
    work_phone = st.selectbox("Work Phone (1 = Yes, 0 = No)", [0, 1])

with col2:
    type_income = st.selectbox("Type of Income", ["Working", "Commercial associate", "State servant", "Pensioner", "Unemployed", "Student"])
    education = st.selectbox("Education Level", ["Higher education", "Secondary education", "Incomplete higher", "Lower secondary", "Academic degree"])
    marital_status = st.selectbox("Marital Status (1 = Married, 0 = Not Married)", [0, 1])
    housing_type = st.selectbox("Housing Type", ["Rented", "Owned", "With Parents"])
    age = st.number_input("Age", 0, 120, 51)
    

with col3:
    phone = st.selectbox("Phone (1 = Yes, 0 = No)", [0, 1])
    email_id = st.selectbox("Email ID (1 = Yes, 0 = No)", [0, 1])
    type_occupation = st.selectbox("Type of Occupation", ["Working", "Commercial associate", "State servant", "Pensioner", "Unemployed", "Student"])
    family_members = st.number_input("Number of Family Members", 0, 20, 2)
    employment_years = st.number_input("Years of Employment", 0.0, 50.0, 0.0)




if st.button("🔍 Predict"):
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

    response = requests.post(API_URL, json=input_data)

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