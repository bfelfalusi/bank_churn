import streamlit as st
import pickle


st.markdown("<h1 style='text-align: center; color: white;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
credit_score = st.slider("Credit Score",350,850)
gender = st.radio("Gender",("Male","Female"))
age = st.number_input("Age",18,100)
tenure = st.number_input("Tenure",0,10)
balance = st.number_input("Balance",0,4)
salary = st.number_input("Estimated Salary",0,4)
if gender == 'Male':
    genderb = 1
else:
    genderb = 0


predictbutton = st.button("Predict")