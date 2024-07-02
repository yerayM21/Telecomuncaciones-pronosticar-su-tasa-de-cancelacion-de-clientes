import pandas as pd 
import numpy as np

def merge_data(data):
    "This function processes the data to clean it and prepare it for merging with other data frames."
    df_Contratos = data[0]
    df_Internet = data[1]
    df_Personal = data[2]
    df_Phone = data[3]
    
    # df_Contratos clean data
    ## Rename
    df_Contratos.rename(columns ={'customerID':'CustomerID'}, inplace=True)
    ## Change data type 
    df_Contratos['BeginDate'] = pd.to_datetime(df_Contratos['BeginDate'],errors='coerce')
    df_Contratos['EndDate'] = pd.to_datetime(df_Contratos['EndDate'], errors='coerce')
    df_Contratos['TotalCharges'] = pd.to_numeric(df_Contratos['TotalCharges'], errors='coerce')
    df_Contratos['Type'] = df_Contratos['Type'].astype('category')
    df_Contratos['PaymentMethod'] = df_Contratos['PaymentMethod'].astype('category')
    
    # df_Internet
    ## Rename
    df_Internet.rename(columns ={'customerID':'CustomerID'}, inplace=True)
    #df_Personal
    ## Rename
    df_Personal.rename(columns = {'customerID':'CustomerID'}, inplace=True)
    df_Personal.rename(columns ={'gender':'Gender'},inplace=True)
    # df_Phone
    ## Rename 
    df_Phone.rename(columns = {'customerID':'CustomerID'},inplace=True)
    
    # Merge data
    # Merge the tables contratos to internet 
    df_Merge = pd.merge(df_Contratos,df_Internet,on='CustomerID',how='outer')
    # Merge the tables df_Merge to Personal
    df_Merge = pd.merge(df_Merge,df_Personal,on='CustomerID',how='outer')
    # Merge the tables df_Merge to Phone
    df_Merge = pd.merge(df_Merge,df_Phone,on='CustomerID',how='outer')
    # Create column Churn rate
    df_Merge['ChurnRate'] = np.where(df_Merge['EndDate'].isna(),0,1)         
    
    df_Merge.to_csv('datasets/Output/merge.csv')
    print('Dataframe created at route: datasets/Output/merge.csv')
    
    return df_Merge



