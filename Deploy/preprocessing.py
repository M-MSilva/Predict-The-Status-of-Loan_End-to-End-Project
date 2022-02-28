# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 09:06:28 2022

@author: marcosmatheus
"""

import numpy as np
import pandas as pd



def runPreprocessing(df):
    dataset = pd.read_csv('https://raw.githubusercontent.com/M-MSilva/Predict-The-Status-of-Loan-End-to-End-Project/master/Dataset/LOAN.csv',  on_bad_lines='skip',decimal='.', thousands=',',encoding='utf-8')

    dataset = dataset.drop(["Loan_Status","Loan_ID"], axis=1) # drop labels for training set
    #dataset = dataset.drop("Loan_Status", axis=1) # drop labels for training set


    dataset_num = dataset.select_dtypes(include=[np.number])
    #dataset_cat = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']
    dataset_cat = dataset.select_dtypes(include=['object'])

    from imblearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import RobustScaler
    from sklearn.impute import SimpleImputer

    num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('rbscaler',RobustScaler()),
            ('std_scaler', StandardScaler()),
            
        ])

    num_pipeline.fit_transform(dataset_num)


    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder


    num_attribs = list(dataset_num)
    cat_attribs = list(dataset_cat)

    full_pipeline = ColumnTransformer([
            ("num", num_pipeline, num_attribs),
            ("cat", OneHotEncoder(), cat_attribs)
        ])


    full_pipeline.fit_transform(dataset)

    df_prepared = full_pipeline.transform(df)
    
    return df_prepared 

