import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


def replacement_of_null_values(data):
    '''This function will prepare the data for model training, focusing on dealing with null values.
    The method that will be used to process the data is at my discretion as to how null values can be replaced.'''
    # Delete the columns that we are not going to use
    data = data.drop(['CustomerID','BeginDate','EndDate'],axis=1)
    # Null values ​​will be changed to No Service, since they are clients who did not contract
    columns_to_replace_nan = ['InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','MultipleLines']
    data[columns_to_replace_nan] = data[columns_to_replace_nan].fillna('NoService')
    # we use the monthlycharges values
    data["TotalCharges"] = data["TotalCharges"].fillna(data['MonthlyCharges'])
    
    # rename the varible
    df_Merge_replacement_null = data
    
    return df_Merge_replacement_null

def SimpleImputer(data):
    numeric = data.select_dtypes(include='number').columns
    categoric = data.select_dypes(exclude='number').columns
    
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_numeric = pd.DataFrame(imp.fit_transform(data[numeric]), columns=numeric)
    
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    impute_categoric = pd.DataFrame(imp.fit_transform(data[categoric]), columns=categoric)
    
    df_impute_data = pd.concat([imp_numeric,impute_categoric], axis=1)
    
    return df_impute_data

