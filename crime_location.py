


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df=pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')
#Determine trends in crime occurrence over time

location_count=df['Location'].value_counts()
print('Top 5 location where crime occur')
print(location_count.head())