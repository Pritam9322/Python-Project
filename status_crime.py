import warnings
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

df = pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')

premise = df['Premis_Desc']
count_of_premises = premise.value_counts()
print(count_of_premises)

# Examine the status of reported crimes.
crime = df['Status']
status_counts = crime.value_counts()
print(status_counts)

plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)  # Corrected autopct format
plt.title('Status of Reported Crimes')
# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.show()
