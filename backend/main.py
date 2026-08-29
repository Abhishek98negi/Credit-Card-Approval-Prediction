from fastapi import FastAPI
from pydantic import BaseModel

from backend.prediction import predict


app = FastAPI(
    title="Credit card Approval prediction",
    version="1.0.0"
)

# input schema matching training features
class CreditCardInput(BaseModel):
    GENDER: object
    Car_Owner:object 
    Propert_Owner:object 
    Annual_income:float
    Type_Income:object 
    EDUCATION:object 
    Marital_status:object 
    Housing_type:object 
    Work_Phone:int  
    Phone:int  
    EMAIL_ID:int  
    Type_Occupation:object 
    Family_Members:int  
    Age:int  
    Employment_years:float


@app.get("/predict")
def predict_check():
    return {"status": "ok"}


# Credit card approval prediction endpoint
@app.post("/predict-credit-card-approval")
def predict_credit_card_approval(input_data: CreditCardInput):
    input_data = input_data.model_dump()
    result = predict(input_data=input_data)
    return {
        "prediction": result["prediction"],
        "probability": result["probability"],
        "diagnosis": (
            "Credit Card Approved"
            if result["prediction"] == 0
            else "Credit Card Rejected"
        )
    }

# uvicorn backend.main:app --reload
# http://127.0.0.1:8000/docs