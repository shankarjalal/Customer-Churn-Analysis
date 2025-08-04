# Gender  --> 1 Female  0 Male
# Churn  -->  1 Yes   0 No
# Scaler is exported as scaler.pkl  
# SVC_Model is exproted as model.pkl
# Order of the  x ==> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'.

import streamlit as st
import joblib
import numpy as np

scaler = joblib.load('ML3project/scaler.pkl')

model = joblib.load('ML3project/model.pkl')

st.title('Churn Prediction App')

st.divider()

st.write('Please enter the values and hit the predict button for getting a predictions.')

st.divider()

age = st.number_input('Enter Age', min_value = 10, max_value = 100, value = 30)

tenure = st.number_input('Enter Tenure', min_value = 0, max_value = 130, value = 10)

monthlycharges  = st.number_input('Enter Monthly Charges', min_value = 30, max_value = 150)

# gender = st.number_input('Enter the Gender', ['Male', 'Female'])
gender = st.selectbox('Select Gender', ['Male', 'Female'])

st.divider()

predictbutton = st.button('Predict !')

if predictbutton:
    # Convert gender to numeric: 1 for Female, 0 for Male
    gender_selected = 1 if gender == 'Female' else 0

    # Prepare input as a list of numeric values
    x = [age, gender_selected, tenure, monthlycharges]

    x1 = np.array(x, dtype=float)  # Ensure all values are float

    x_array = scaler.transform([x1])

    prediction = model.predict(x_array)[0]

    predicted = 'Yes' if prediction == 1 else 'No'

    st.write(f'Prediction : {predicted}')
else:
    st.write('Please Enter the values and use predict button.')


