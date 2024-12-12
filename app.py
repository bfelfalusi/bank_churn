import streamlit as st
import pickle


st.markdown("<h1 style='text-align: center; color: white;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
credit_score = st.slider("Credit Score",350,850)
gender = st.radio("Gender",("Male","Female"))
age = st.number_input("Age",18,100)
tenure = st.number_input("Tenure",0,10)
st.write("0-50000: 0, 50001-100000: 1 ... 200001-250000: 4")
balance = st.number_input("Balance",0,4)
credit_card = st.radio("Do you have a credit card?",("Yes","No"))
active_member = st.radio("Are you currently customer of the bank?",("Yes","No"))
st.write("0-40000: 0, 40001-80000: 1 ... 160001-200000: 4")
salary = st.number_input("Estimated Salary",0,4)
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

predictbutton = st.button("Predict")