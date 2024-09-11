
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df=pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')
#Determine trends in crime occurrence over time
#Convert date columns to datetime objects
df['Date_Rptd']=pd.to_datetime (df['Date_Rptd'])
df['Date_Rptd']=pd.to_datetime (df ['DATE_OCC'])

#Aggregate by match
monthly_crime=df.resample('M', on='Date_Rptd').size()

#plot the trend
plt.figure(figsize=(10,6))
plt.plot(monthly_crime.index,monthly_crime.values, marker='H',color='#54B435')
plt.title("Crime Occurrence Over Time")
plt.xlabel("Month")

plt.show()