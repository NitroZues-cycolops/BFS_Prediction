import pickle
import pandas as pd

Model_version = "1.3.4"

with open("model/model.pkl","rb") as file:
    model = pickle.load(file)

def ml_predict(user_input: dict):
    input_df = pd.DataFrame(user_input)
    prediction = model.predict(input_df)[0]
    return prediction