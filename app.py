import streamlit as st
st.title("streamlit app tut")
st.write("this is my new app")
button1 = st.button("Predict")
st.header("(estimated) Income")
est_inc =  st.slider("what is the estimated income?",0,4)