import pandas as pd
#Data colection and preparation based on final project
#Loading data sets
data_2023 = pd.read_csv('/Users/claudiogf/Desktop/dataparking/parking-tickets_2023.csv', delimiter=';')
data_2024 = pd.read_csv('/Users/claudiogf/Desktop/dataparking/parking-tickets_2024.csv', delimiter=';')
#Combine both years for a full analysis between this two years used on the project
all_tickets = pd.concat([data_2023, data_2024])
#Descriptive statistics
print("descriptive statistics:")
print(all_tickets.describe())
#Summary of the number of tickets per year
print("\nTicket Count per Year:")
print(all_tickets['Year'].value_counts())
#Most Common Infractions between 2023 and 2024
print("\nMost Common Infractions:")
print(all_tickets['InfractionText'].value_counts().head(10))
#Summary statistics for tickets by street 
print("\nTickets per Street:")
print(all_tickets['Street'].value_counts().head(10))

#DATA VISTUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns

#Convert EntryDate to datetime
all_tickets['EntryDate'] = pd.to_datetime(all_tickets['EntryDate'])
#Based on the convert, make the column for the month and years
all_tickets['Month'] = all_tickets['EntryDate'].dt.month
all_tickets['Year'] = all_tickets['EntryDate'].dt.year
#Number of tickets by month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', hue='Year', data=all_tickets, palette='Set2')
plt.title('Number of Tickets by Month (2023 vs 2024)')
plt.xlabel('Month')
plt.ylabel('Number of Tickets')
plt.show()
#top 10 streets with the most tickets
top_streets = all_tickets['Street'].value_counts().nlargest(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_streets.index, y=top_streets.values, palette='Set3')
plt.title('Top 10 Streets with the Most Parking Tickets')
plt.xlabel('Street')
plt.ylabel('Number of Tickets')
plt.xticks(rotation=45)
plt.show()

# top 10 streets with common infractions between 2023, 2024
top_infractions = all_tickets['InfractionText'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_infractions.index, y=top_infractions.values, palette='Set1')
plt.title('Top 10 Most Common Parking Violations')
plt.xlabel('Infraction')
plt.ylabel('Number of Tickets')
plt.xticks(rotation=45)
plt.show()

#CORRELATION ANALYSIS AND HEATMAP 
#Make correlation matrix for all tickets
numeric_columns = ['Block', 'Year']
correlation_matrix = all_tickets[numeric_columns].corr()

#heatmap development for the previous matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap for Numeric Variables')
plt.show()

# Optional: Convert 'Status' to a numeric variable (1 for "IS", 0 for other statuses if applicable)
all_tickets['Status_Numeric'] = all_tickets['Status'].apply(lambda x: 1 if x == 'IS' else 0)

# Calculate the number of infractions per street
all_tickets['Infraction_Count_Street'] = all_tickets.groupby('Street')['Street'].transform('count')

# Create a DataFrame with the numeric columns we want to include in the heatmap
correlation_data = all_tickets[['Block', 'Year', 'Month', 'Status_Numeric', 'Infraction_Count_Street', 'Bylaw']]

# Generate the correlation matrix
correlation_matrix = correlation_data.corr()

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Detailed Correlation Heatmap for Parking Tickets')
plt.show()