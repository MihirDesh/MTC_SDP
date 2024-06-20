import joblib
import pandas as pd
import numpy as np
import streamlit as st


model = joblib.load('models/random_forest_model.joblib')

st.set_page_config(layout="wide")

st.title('Predicting Credit Worthines of a Customer')
st.header('Features: ')
col1,col2 = st.columns(2,gap = "large")
with col1:
    dlqin = st.selectbox('Serious Dlqin 2yrs ?',(0,1),key = "dlqin")
    age = st.number_input('Enter your age',key = "age_input",min_value = 0,max_value = 100)
    past_due_30 = st.number_input('Number of times past due (30-59)',key = "past_due_30",min_value = 0,max_value = 100)
    dt_ratio = st.number_input('Debt Ratio',key = "debt_ratio")
    income = st.number_input('Monthly Income',key = "income",min_value = 0)
    credit_lines = st.number_input('Number Of Open Credit Lines And Loans',key = "credit_lines",min_value = 0)
    ninety = st.number_input('Number Of times 90 days late',key = "ninety_late",min_value = 0)
    real_estate = st.number_input('Number Of real estate loans or lines',key = "real_estate_loans",min_value = 0)
    sixety = st.number_input('Number Of Time 60-89 Days Past Due Not Worse',key = "sixety_due",min_value = 0)
    dependants = st.number_input('Number of Dependants',key = "dependants",min_value = 0)
   
    credit_history = st.number_input('Credit History Length',key = "credit_history_length",min_value = 0 )
    payment_score = st.number_input('Payment History Score',key = "payment_history_score")
    ltv =  st.number_input('LTV',key = "ltv")

with col2:
    unsec_lines = st.number_input('Revolving Utilization Of Unsecured Lines',key = "unsec_lines")
    t_assets = st.number_input('total assets',key = "t_assets")
    liabs = st.number_input('total liabilites',key = "t_liab")
    retired = st.selectbox('Retired?',(True,'False'),key = "retired")
    student = st.selectbox('student?',(True,'False'),key = "student")
    unemployed  = st.selectbox('Unemployed?',(True,'False'),key = "unemployed")
    masters_degree  = st.selectbox('Masters Degree?',(True,'False'),key = "masters_degree")
    bachelor_degree  = st.selectbox('Bachelor Degree?',(True,'False'),key = "bachelor_degree")
    high_school  = st.selectbox('High School?',(True,'False'),key = "high_school")
    phd  = st.selectbox('PHD?',(True,'False'),key = "phd")
    cust_feedback = st.text_input('Enter Customer Feedback',key = "feedback")
    cust_serv_log = st.text_input('Customer service log',key = "customer_service_log")
    ffs = st.number_input('Feedback sentiment score',key = 'ffs')
    sls = st.number_input('Service log score',key = 'sls')



if(st.button('Predict',type="primary")):
    x_array = np.array([[dlqin,unsec_lines,age,past_due_30,dt_ratio,income,credit_lines,ninety,real_estate,t_assets,liabs,student,unemployed,bachelor_degree,high_school,masters_degree,phd,ffs,sls]])
    result = model.predict(x_array)
    st.write("Dear Customer, your credit score is = ")
    st.text(result)


    









    












