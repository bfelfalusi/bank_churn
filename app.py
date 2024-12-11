import streamlit as st
import pickle


st.markdown("<h1 style='text-align: center; color: white;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
credit_score = st.slider("credit_score",0,850)
gender = st.radio("What is the gender?",("Male","Female"))
if gender == 'Male':
    genderb = 1
else:
    genderb = 0


predictbutton = st.button("Predict")