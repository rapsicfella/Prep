import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# Perform data analysis
average_age = df['Age'].mean()
city_counts = df['City'].value_counts()

print("Average Age:", average_age)
print("City Counts:\n", city_counts)