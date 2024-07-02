import pandas as pd 
from data.load_data import load_data
from data.merge_data import merge_data
from EDA.Eda_report import eda_report

datas= load_data()
data = merge_data(datas)
eda_report(data)