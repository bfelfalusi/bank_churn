import numpy as np
#import joblib
import streamlit as st
import pandas as pd

#loaded_model = joblib.load('svc_joblib.joblib')

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
    credit_score = st.slider("Credit Score",350,850)
    gender = st.radio("Gender",("Male","Female"))
    age = st.number_input("Age",18,100)
    tenure = st.number_input("Tenure",0,10)
    balance = st.number_input("Balance:  0-50000: 0, 50001-100000: 1 ... 200001-250000: 4",0,4)
    product_num = st.number_input("Number of products owned",1,4)
    credit_card = st.radio("Do you have a credit card?",("Yes","No"))
    active_member = st.radio("Are you currently customer of the bank?",("Yes","No"))
    salary = st.number_input("Estimated Salary:  0-40000: 0, 40001-80000: 1 ... 160001-200000: 4",0,4)
    country = st.selectbox("Country",("Germany","Spain","France"))
    if gender == 'Male':
        genderb = 1
    else:
        genderb = 0
    if active_member == "Yes":
        activeb = 1
    else:
        activeb = 0
    if credit_card == "Yes":
        creditb = 1
    else:
        creditb = 0
    if country.lower() == 'germany':
        countryb = (1,0)
    elif country.lower() == 'spain':
        countryb= (0,1)
    else:
        countryb = (0,0)

    features = [[]]
    predictbutton = st.button("Predict")
    

if __name__ == '__main__':
        main()
