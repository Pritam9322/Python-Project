import pandas as pd
import folium
import warnings
import os

warnings.filterwarnings('ignore')

df = pd.read_csv(r'E:\Odin School\Python\Mini Capstone project\crime_data\crime_data.csv')

# Creating a folium map centered around the average latitude and longitude of crime data
crime_map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=10)

# Adding crime markers to the map
for index, row in df.iterrows():
    popup = folium.Popup(f"Type: {row['Crm_Cd_Desc']}, Location: {row['Location']}, Date: {row['DATE_OCC']}", parse_html=True)
    # ADD A marker for each crime with popup message
    folium.Marker(location=[row['LAT'], row['LON']], popup=popup).add_to(crime_map)

# Save the map as an HTML file
crime_map.save("crime_map.html")



print("Current Working Directory:", os.getcwd())
