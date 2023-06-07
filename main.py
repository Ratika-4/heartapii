# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Age : int
    sex : int
    chest_pain: int
    resting_bp : int
    cholestoral : int
    fasting_bs : float
    resting_electrocardiographic :  float
    maximum_heartrate: int
    exercise_inducedangina:int
    oldpeak:int
    slope:int
    colored_flourosopy:int
    thal:int


# loading the saved model
heart_model = pickle.load(open('trained_model.sav','rb'))


@app.post('/heartDisease_prediction')
def heart_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    chest_pain= input_dictionary[' chest_pain']
    resting_bp= input_dictionary['resting_bp']
    cholestoral = input_dictionary[' cholestoral']
    fasting_bs  = input_dictionary[' fasting_bs ']
    resting_electrocardiographic = input_dictionary['resting_electrocardiographic']
    maximum_heartrate = input_dictionary['maximum_heartrate']
    exercise_inducedangina = input_dictionary[' exercise_inducedangina']
    oldpeak = input_dictionary['oldpeak']
    slope= input_dictionary[' slope']
    colored_flourosopy= input_dictionary['colored_flourosopy']
    thal = input_dictionary['thal']

    input_list =[age,sex,chest_pain,resting_bp,cholestoral,fasting_bs,resting_electrocardiographic,maximum_heartrate,exercise_inducedangina,oldpeak,slope,colored_flourosopy,thal]
    prediction = heart_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person has not disease'
    
    else:
        return 'The person has disease'