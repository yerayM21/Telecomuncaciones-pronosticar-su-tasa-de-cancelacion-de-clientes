import pandas as pd 

def load_data():
    "The function will Upload datasets."
    df_Contratos = pd.read_csv('datasets/Input/contract.csv')
    df_Internet = pd.read_csv('datasets/Input/internet.csv')
    df_Personal = pd.read_csv('datasets/Input/personal.csv')
    df_Phone = pd.read_csv('datasets/Input/phone.csv')
    
    return df_Contratos, df_Internet, df_Personal, df_Phone


