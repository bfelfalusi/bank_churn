import streamlit as st
import pickle


st.markdown("<h1 style='text-align: center; color: white;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
credit_score = st.slider("Credit Score",350,850)
gender = st.radio("Gender",("Male","Female"))
age = st.number_input("Age",0,100,int)
if gender == 'Male':
    genderb = 1
else:
    genderb = 0


predictbutton = st.button("Predict")