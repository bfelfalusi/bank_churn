import streamlit as st
import pickle

@st.cache(allow_output_mutation=True)
def load_model(model_name):
    with open(model_name, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

model = load_model('best_rf_model.pkl')

gender = st.radio("What is the gender?",("Male","Female"))