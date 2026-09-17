from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from Schema.user_input import UserInput 
from Schema.prediction_response import predict_response
from model.predict import ml_predict,Model_version

# import the ml model
app = FastAPI()

@app.post("/predict", response_model=predict_response)
def predict(data:UserInput):
    user_input=pd.DataFrame([{
        'Gender': data.Gender,
        'Age': data.age_bin,
        'Occupation': data.Occupation,
        'City_Category': data.City_Category,
        'Stay_In_Current_City_Years': data.Stay_In_Current_City_Years,
        'Marital_Status': data.Marital_Status,
        'Product_Category_1': data.Product_Category_1,
        'Product_Category_2': data.Product_Category_2,
        'Product_Category_3': data.Product_Category_3
    }])

    try:
        prediction = ml_predict(user_input)
        return JSONResponse(status_code=200, content={"Prediction Succesfull":prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content= str(e))
    
# human readable
@app.get("/")
def home():
    return {"message":"BFS prediction backend using FastAPI"}

# Machine readable
@app.get("/health")
def health_check():
    return {
        "status":"ok",
        "Connected to":"ML",
        "version":Model_version
    }