import pickle
import streamlit as st
import pandas as pd



gender = ['male', 'female']
Married = ['Yes', 'No']
Dependents = ['1', '2', '3', '4', '5']
Education = ['Graduation', 'Non Graduation']
Employment = ['Yes', 'No']
Credit_History = ['0', '1']
Property_Area = ['Urban', 'Semiurban', 'Rural']

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    gender = st.selectbox('Select your Gender', sorted(gender))
with col2:
    Married = st.selectbox('Select your Marriage Criteria', sorted(Married))
with col3:
    Dependents = st.selectbox('Select your Dependents Criteria', sorted(Dependents))
with col4:
    Education = st.selectbox('Select your Education Criteria', sorted(Education))
with col5:
    Employment = st.selectbox('Select your Employment Criteria', sorted(Employment))

col6, col7, col8, col9, col10, col11 = st.columns(6)
with col6:
    ApplicantIncome = st.number_input('Income')
with col7:
    CoapplicantIncome = st.number_input('CoApplicantIncome')
with col8:
    LoanAmount = st.number_input('Enter your loan amount')
with col9:
    Loan_Amount_Term = st.number_input('LoanAmountTerm')
with col10:
    Credit_History = st.selectbox('Credit Score', sorted(Credit_History))
with col11:
    Property_Area = st.selectbox('Property Area', sorted(Property_Area))

if st.button('Predict Loan Approval'):
    # Create a DataFrame with the user input
    input_data = {
        'Gender': [gender],
        'Married': [Married],
        'Dependents': [Dependents],
        'Education': [Education],
        'Self_Employed': [Employment],  # Use the corrected variable name here
        'ApplicantIncome': [ApplicantIncome],
        'CoapplicantIncome': [CoapplicantIncome],
        'LoanAmount': [LoanAmount],
        'Loan_Amount_Term': [Loan_Amount_Term],
        'Credit_History': [Credit_History],
        'Property_Area': [Property_Area]
    }
    user_input_df = pd.DataFrame(input_data)

    # Make predictions using your model
    prediction = LR.predict(user_input_df)

    # Display the prediction result
    if prediction[0] == 1:
        st.success('Loan Approved!')
    else:
        st.error('Loan Rejected!')




