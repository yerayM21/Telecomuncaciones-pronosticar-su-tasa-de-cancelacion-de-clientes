import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sys 
import time


def eda_report(data):
    'The EDA report will create some files to analyze the table data and create the visualization.'
    
    # data info 
    ## repote describe 
    describe = data.describe()
    
    ## Exporting the file 
    with open('src/EDA/Files/descibre.txt', 'w') as f:
        f.write(describe.to_string())
    
    ## Exporting general info 
    with open('src/EDA/Files/info.txt','w') as f:
        sys.stdout = f
        data.info()
        sys.stdout = sys.__stdout__
    
    # Pie chart for ChurnRate
    counts = data['ChurnRate'].value_counts()
    labels = ['Clientes que siguen','Clientes que han dejado']
    sizes = [counts.get(0,0),counts.get(1,0)]
    colors = ['#6cb6f4','#ee4242']
    explode = (0.1,0)
    
    plt.figure(figsize=(6,6))
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.title('Porcentaje de abandono de clientes')
    plt.axis('equal')
    plt.savefig('src/EDA/Files/Pie_chart.png')
    plt.close()
    
    # Filter data and calculate contract duration.
    data['Duration'] = (data['EndDate'] - data['BeginDate']).dt.days
    data['Duration_months'] = data['Duration'] // 30
    # Creation of the histogram to visualize the duration of the contract
    plt.figure(figsize=(20, 8))
    plt.hist(data['Duration_months'], bins=range(1,30), edgecolor='black')
    plt.title('Duración del contrato en meses')
    plt.xlabel('Meses')
    plt.ylabel('Frecuencia')
    plt.xticks(range(1,30))
    plt.grid(True)
    plt.savefig('src/EDA/Files/Hist_ContractDuration.png')
    plt.close()
    
    # Generate histograms for different purposes to analyze customer cancellation
    # To finish the number of graphs
    fig, (ax0, ax1, ax2, ax3) = plt.subplots(1, 4, figsize=(16, 4))
    
    sns.histplot(data=data, x="PaymentMethod", hue="ChurnRate", multiple="fill",ax=ax0,palette=colors)
    sns.histplot(data=data, x="Type", hue="ChurnRate", multiple="fill", ax=ax1,palette=colors)
    sns.histplot(data=data, x="Gender", hue="ChurnRate", multiple="fill", ax=ax2,palette=colors)
    sns.histplot(data=data, x="InternetService", hue="ChurnRate", multiple="fill", ax=ax3,palette=colors)
    
    ax0.set_xticklabels(ax0.get_xticklabels(), rotation= 90)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation= 90)
    
    ax1.legend([1,0],loc='upper right', title='Churn Rate')
    fig.suptitle("Cancelacion de clientem Por Metodos de pago,Tipo de Contrato, Genero y Servicio de internet")
    plt.savefig('src/EDA/Files/Hist_DifferentPurposesCancellation.png',bbox_inches='tight')
    plt.close()
    
    # boxplot
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 4))
    custom_palette = {'0': '#6cb6f4', '1': '#ee4242'}
    sns.boxplot(data=data, x="ChurnRate", y="MonthlyCharges", ax=ax0,palette=custom_palette)
    sns.boxplot(data=data, x="ChurnRate", y="TotalCharges", ax=ax1,palette=custom_palette)
    fig.suptitle("Cargos mensuales y Cargos Totales Influyen en la Cancelacion Cliente")
    plt.savefig('src/EDA/Files/BoxplotCharges.png',bbox_inches='tight')
    plt.close()
    
    print('EDA report created at route: /src/eda/files')
 



