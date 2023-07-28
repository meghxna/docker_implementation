# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:34:13 2023

@author: Meghana
"""


from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app=Flask(__name__)
Swagger(app)
with open('classifier18.pkl','rb') as file:
    classifier = pickle.load(file)

@app.route('/')
def index():
    return 'welcome'








@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        299:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))



if __name__ == '__main__':
    app.run()