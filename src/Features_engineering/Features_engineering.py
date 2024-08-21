import pandas as pd 
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def scalar(columns):
    "Function to normalize numeric values"
    scalar = StandardScaler()
    scalar_cols= scalar.fit_transform(columns)
    return scalar_cols

def OHE(data):
    "Function to encode categoric values"
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_columns = encoder.fit_transform(data)
    return pd.DataFrame(encoded_columns, columns=encoder.get_feature_names(), index=data.index)

def data_processing(data):
    numeric=data.select_dtypes(include='number')
    categoric =data.select_dtypes()
    

