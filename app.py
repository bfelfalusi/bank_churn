import streamlit as st
import pickle
import requests
import random

model_url = "https://github.com/bfelfalusi/bank_churn/blob/main/best_vclf_model.pkl"


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

lista = [[]]
predictbutton = st.button("Predict")

st.write("Bank churn result: ")

if predictbutton:
    lista[0].append(credit_score)
    lista[0].append(genderb)
    lista[0].append(age)
    lista[0].append(tenure)
    lista[0].append(balance)
    lista[0].append(product_num)
    lista[0].append(creditb)
    lista[0].append(activeb)
    lista[0].append(salary)
    lista[0].append(countryb[0])
    lista[0].append(countryb[1])
    
st.write(random.randint(0,1))