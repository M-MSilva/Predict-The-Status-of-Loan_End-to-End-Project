# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:03:02 2022

@author: marquinho
"""


import pickle 
import pandas as pd
import streamlit as st
import preprocessing as pre



#loaded_model = pickle.load(open('trained_model.sav','rb'))

#we found where the file trained_model.sav is
current_directory = Path(__file__).parent #Get current directory
loaded_model = open(os.path.join(current_directory, 'trained_model.sav'), 'rb') #rb = read bytes because we are reading the file



def Loan_prediction(input_data):
    
    
    
    prediction = loaded_model.predict(input_data)


    if (prediction == 1):      
    	return 'The person IS eligible to receive the loan'
    else:
    	return 'The person is NOT eligible to receive the loan'
  
    
    
def code():	   
    #name of the page
    st.title('Loan Prediction Web App') 
    
    form = st.form(key='user')
    Gender = form.selectbox('What is your gender?',['Male','Female'])
    Married = form.selectbox('Are you married',['Yes','No'])
    Dependents = form.selectbox('How many children or dependents do you have?',['1','2','3+']) 
    Education = form.selectbox('Do you have a degree?',['Graduate','Not Graduate'])
    Self_Employed = form.selectbox('Do you work for yourself?',['Yes','No'])
    Credit_History = form.selectbox('Does the individual have a good credit history? 1 for good or 0 for bad',[1,0])
    Property_Area = form.selectbox('Does the applicant live ?',['Urban', 'Semiurban','Rural'])
    submit_button = form.form_submit_button('Add')
    
    
    with st.form(key='numbers'):        
        ApplicantIncome	= st.number_input('what is your salary?')
        CoapplicantIncome	= st.number_input('What is your partners salary? If you dont have a partner, enter 0.')
        LoanAmount	= st.number_input('What is the requested amount?')
        Loan_Amount_Term	= st.number_input('how long do you plan to pay off the debt? in days.', min_value=0, max_value=10000, value=0, step=1)
        submit_button2 = st.form_submit_button('Add')
    
    data = [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]
    columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
    
    
    #insert
    df = pd.DataFrame(data=data, columns=columns)
    
    
    #treatment of the data
    if(Property_Area):
        df_prepared = pre.runPreprocessing(df)
    


    #code for prediction
    Condition = ''
    
    #creating a button for prediction
    if st.button('My Eligibility Is?'):
        Condition = Loan_prediction(df_prepared)
    
    st.success(Condition)

if __name__ == '__main__':
    code()				
    



   


				
    
    
    
    
    
