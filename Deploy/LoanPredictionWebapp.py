
import pickle 
import pandas as pd
import streamlit as st
import preprocessing as pre


loaded_model = pickle.load(open('trained_model.sav','rb'))



def Loan_prediction(input_data):
    
    
    
    prediction = loaded_model.predict(input_data)


    if (prediction == 1):      
    	return 'The person IS eligible to receive the loan'
    else:
    	return 'The person is NOT eligible to receive the loan'
  
    
    
def code():	   
    #name of the page
    st.title('Loan Prediction Web App') 
    
    Gender	= st.text_input('What is your gender, Male or Female?')
    Married	= st.text_input('Are you married, Yes or No?')
    Dependents	= st.text_input('How many children do you have,1,2 or 3+ ?')
    Education	= st.text_input('Do you have a degree? Graduate or Not Graduate')
    Self_Employed	= st.text_input('Do you work for yourself? Yes or No')
    ApplicantIncome	= st.number_input('what is your salary?')
    CoapplicantIncome	= st.number_input('What is your partners salary? If you dont have a partner, enter 0.')
    LoanAmount	= st.number_input('What is the requested amount?')
    Loan_Amount_Term	= st.number_input('how long do you plan to pay off the debt? in days.', min_value=0, max_value=10000, value=0, step=1)
    Credit_History	= st.number_input('Does the individual have a good credit history? 1 for good or 0 for bad', min_value=0, max_value=3, value=0, step=1)
    Property_Area	= st.text_input('Does the applicant live in an Urban, Semiurban or Rural area?')
    
    #insert and treatment of the data
    data = [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]
    columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
    
    df = pd.DataFrame(data=data, columns=columns)
    
    if(Property_Area):
        df_prepared = pre.runPreprocessing(df)




    #code for prediction
    Condition = ''
    
    #creating a button for prediction
    if st.button('Loan Test Result'):
        Condition = Loan_prediction(df_prepared)
    
    st.success(Condition)


if __name__ == '__main__':
    code()				
    



   


				
    
    
    
    
    