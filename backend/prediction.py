import os
import pandas as pd
import joblib

# 1. Get the absolute path to the directory where THIS python script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Join that directory with your filename
model_path = os.path.join(BASE_DIR, "xgb_best.joblib")

# 3. Load the model using the dynamic path
model = joblib.load(model_path)

# model = joblib.load("D:\\My Learning\\ML projects\\Credit-Card-Approval-Prediction\\backend\\xgb_best.joblib")

def predict(input_data: dict):
    df = pd.DataFrame([input_data])

    # get predicted class
    prediction = int(model.predict(df)[0])
    # get prediction probability of credit card approval
    probability = float(model.predict_proba(df)[0][0])

    return {
        "prediction": prediction,
        "probability": probability
    }

					
# example usage
# sample_input = {
#     "GENDER": 'M',
#     "Car_Owner": 'Y',
#     "Propert_Owner": 'Y',
#     "Annual_income": 180000.0,
#     "Type_Income": "Pensioner",
#     "EDUCATION": "Higher education",
#     "Marital_status": "Married",
#     "Housing_type": "House / apartment",
#     "Work_Phone": 0,
#     "Phone": 0,
#     "EMAIL_ID": 0,
#     "Type_Occupation": "Unknown",
#     "Family_Members": 2,
#     "label": 1,
#     "Age": 51,
#     "Employment_years":0.0
# }
# result = predict(input_data=sample_input)
# print(result)