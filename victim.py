import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')


#Investigate the distribution of victim ages and genders.
#Plot distribution of victim ages
plt.figure(figsize=(10,6))
sns.histplot(df['Vict_Age'], color='#FF6000', edgecolor='black')
plt.title('Distribution of Victim Ages')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
#Plot distribution of victim genders
plt.figure(figsize=(6,6))
sns.countplot(x=df['Vict_Sex'],palette=['#5356FF','#201658','#0D9276'],edgecolor='black')
plt.title('Distribution of Victim Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(True)
plt.show()