

import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df=pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')

print('Information of given database')
print(df.info())
print('\n')

# Retrieve basic statistics on the dataset, such as the total number of records
print('Total number of record in given database')
print(df.shape)  # for records
print('\n')

# Unique values in specific columns.
df1=pd.DataFrame(df)
unique_values=df1["Crm_Cd"].unique()
print("Unique values from crime code column")
print(unique_values)
print('\n')


unique_values_of_Desc=df1["Crm_Cd_Desc"].unique()
print("Unique Values From Crime Code Description Columns:-")
print(unique_values_of_Desc)
print("\n")

#Identity the distinct crime codes and their descriptions.
print("distinct crime codes and their descriptions.")
df2=pd.DataFrame(data=unique_values_of_Desc, index=unique_values,columns=["Description"])
print(df2)

