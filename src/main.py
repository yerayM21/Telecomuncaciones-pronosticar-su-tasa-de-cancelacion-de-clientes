import pandas as pd 
from data.load_data import load_data
from data.merge_data import merge_data
from EDA.Eda_report import eda_report
from Features_engineering.handle_null_values import replacement_of_null_values
from Features_engineering.Features_engineering import OHE

datas= load_data()
data = merge_data(datas)
data = replacement_of_null_values(data)
data = OHE(data)
data.info()
#eda_report(data)