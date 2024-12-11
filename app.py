import streamlit as st
import pickle


st.title("Bank Customer Churn Prediction")
gender = st.radio("What is the gender?",("Male","Female"))
if gender == 'Male':
    genderb = 1
else:
    genderb = 0
predictbutton = st.button("Predict")
if predictbutton:
    st.write(genderb)