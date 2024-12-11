import streamlit as st
import pickle


st.title("Bank Customer Churn Prediction")
gender = st.radio("What is the gender?",("Male","Female"))

predictbutton = st.button("Predict")