
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df=pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')

code=df['Crm_Cd']
count_of_code=code.value_counts()
print(count_of_code)

plt.figure(figsize=(9,7))
count_of_code.plot(kind='bar',color='skyblue')
plt.title('Distribution of Reported Crime Code')
plt.xlabel('Code')
plt.ylabel('Number of crime')
plt.show()
