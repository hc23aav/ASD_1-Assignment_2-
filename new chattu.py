
import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:\Downloads\weather-anomalies-1964-2013 (1).csv"
data = pd.read_csv(file_path)

print(data.describe())

print(data.info())

plt.figure(figsize=(8, 6))
plt.hist(data['max_temp'], bins=20, edgecolor='black')
plt.title('Distribution of Max Temperature')
plt.xlabel('Max Temperature')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(data['max_temp'], data['min_temp'], alpha=0.7)
plt.title('Max Temperature vs Min Temperature')
plt.xlabel('Max Temperature')
plt.ylabel('Min Temperature')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
data.boxplot(column='max_temp', by='type')
plt.title('Temperature Distribution by Type')
plt.xlabel('Type')
plt.ylabel('Max Temperature')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


data['date_str'] = pd.to_datetime(data['date_str'])
data_sorted = data.sort_values(by='date_str')

plt.figure(figsize=(10, 6))
plt.plot(data_sorted['date_str'], data_sorted['degrees_from_mean'])
plt.title('Degrees from Mean Over Time')
plt.xlabel('Date')
plt.ylabel('Degrees from Mean')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(data['longitude'], data['latitude'], c=data['max_temp'], cmap='coolwarm', alpha=0.5)
plt.colorbar(label='Max Temperature')
plt.title('Latitude vs Longitude Colored by Max Temperature')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()


type_distribution = data['type'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(type_distribution, labels=type_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Weather Types')
plt.axis('equal')
plt.show()