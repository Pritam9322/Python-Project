import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df=pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')

#Utilize the geographical information (Latitude an Longitude) to perform spatial analysis
#using matplotlib
plt.figure(figsize=(10,8))
plt.scatter(df['LON'],df['LAT'],s=15,alpha=0.5,c='blue')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Crime Occurence")
plt.grid(True)
plt.show()
#Using Plotly.express create a scatter plot
fig=px.scatter(df,x='LON',y='LAT',title='Crime Occurrences (Spatial)')
# Show the graph
fig.show()