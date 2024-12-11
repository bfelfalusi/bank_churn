import streamlit as st
import pickle


st.title("Bank Customer Churn Prediction")
gender = st.radio("What is the gender?",("Male","Female"))
if gender == "Male":
    gender = 1
else:
    gender = 0
button2 = st.button("press")
if button2:
    st.write(gender)
predictbutton = st.button("Predict")