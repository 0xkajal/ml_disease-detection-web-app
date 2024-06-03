# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:51:16 2024

@author: Lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models

diabetes_model_path = r'diabetes_model_no_scaler.sav'
heart_model_path = r'heart_model.sav'
parkinsons_model_path = r'parkinsons_model_no_scaler.sav'

with open(diabetes_model_path, 'rb') as file:
    diabetes_model = pickle.load(file)

with open(heart_model_path, 'rb') as file:
    heart_model = pickle.load(file)

with open(parkinsons_model_path, 'rb') as file:
    parkinsons_model = pickle.load(file)

# Sidebar for navigation

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes prediction page

if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Level")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the Person")

    # Code for prediction
    diab_diagnosis = ''

    # Creating button for prediction
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float and prepare for prediction
            inputs = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            # Make prediction
            diab_prediction = diabetes_model.predict([inputs])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is not Diabetic'
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

    st.success(diab_diagnosis)

# Heart disease prediction page

if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age of the Person")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Type")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment")
    with col3:
        ca = st.text_input("Major Vessels Colored by Fluoroscopy")
    with col1:
        thal = st.text_input("Thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversible Defect")

    # Code for prediction
    heart_diagnosis = ''

    # Creating button for prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float and prepare for prediction
            inputs = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            # Make prediction
            heart_prediction = heart_model.predict([inputs])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person has Heart Disease'
            else:
                heart_diagnosis = 'The Person does not have Heart Disease'
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

    st.success(heart_diagnosis)

# Parkinson's disease prediction page

if selected == 'Parkinsons Disease Prediction':
    # Page title
    st.title('Parkinsons Disease Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP RAP')
    with col2:
        PPQ = st.text_input('MDVP PPQ')
    with col3:
        DDP = st.text_input('Jitter(DDP)')
    with col4:
        Shimmer = st.text_input('MDVP Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer(APQ3)')
    with col2:
        APQ5 = st.text_input('Shimmer(APQ5)')
    with col3:
        APQ = st.text_input('MDVP(APQ)')
    with col4:
        DDA = st.text_input('Shimmer(DDA)')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Code for prediction
    parkinsons_diagnosis = ''

    # Creating button for prediction
    if st.button('Parkinsons Disease Test Result'):
        try:
            # Convert inputs to float and prepare for prediction
            inputs = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
            # Make prediction
            parkinsons_prediction = parkinsons_model.predict([inputs])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The Person has Parkinsons Disease'
            else:
                parkinsons_diagnosis = 'The Person does not have Parkinsons Disease'
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

    st.success(parkinsons_diagnosis)
