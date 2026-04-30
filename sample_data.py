import pandas as pd

# Load the CSV file
data = pd.read_csv('data/health_data.csv')

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Count missing values in each column
missing_values = data.isnull().sum()

# Display the number of missing values
print("\nNumber of missing values in each column:")
print(missing_values)