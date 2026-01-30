import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Loan Approval Prediction")

income = st.number_input("Applicant Income")
loan = st.number_input("Loan Amount")
credit = st.selectbox("Credit History", [0, 1])

if st.button("Predict"):
    prediction = model.predict([[income, loan, credit]])
    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
