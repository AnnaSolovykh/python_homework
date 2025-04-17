# Creating a simple Series
import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
# print(s)

data1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(data1)
# Output:
# a    10
# b    20
# c    30

data2 = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
# print(data2)
# Output:
# 5 Tom
# 2 Li
# 2 Antonio
# 3 Mary
# print(data2[2])
# Output:
# 2 Li
# 2 Antonio
# print(data2[1])
# This gives a key error!

data3 = data2.reset_index()
# print(data3)
# output:
# 0 Tom
# 1 Li
# 2 Antonio
# 3 Mary
# If some index label is not unique, and you request the value of the 
# series for that index label, what is returned is another series. This is called levels in Pandas. 
# In Pandas, Series are value-mutable, meaning that you can change the value stored at a particular 
# location, but are not size or order mutable.

# List Example
my_list = [10, 20, 30]
# print(my_list[1])  # Access by position
# Output: 20

# Series Example
my_series = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(my_series["b"])  # Access by index label
# Output: 20

# print(my_series.iloc[2]) # Access by integer position
# Output: 30

# Creating a DataFrame from a dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
# print(df)

data_alice = {'Name': 'Alice', 'Age': 24, 'City': 'New York'}
data_bob = {'Name': 'Bob', 'Age': 27, 'City': 'San Francisco'}
data_charlie = {'Name': 'Charlie', 'Age': 22, 'City': 'Chicago'}
df = pd.DataFrame([data_alice, data_bob, data_charlie])
# print(df)
# output: same as before

import numpy as np # load the numpy library
# Create a Pandas DataFrame using NumPy arrays
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# print(df)

# Pandas makes it easy to read data from files. For instance, to read data from a CSV file:
# Read data from a CSV file
df = pd.read_csv('data.csv')

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
})

more_data = pd.DataFrame({
  'Name': ['Fred', 'Barney'],
  'Age': [57, 55],
  'City': ['Bedrock', 'Bedrock']
})

df = pd.concat([data, more_data], ignore_index=True)

# Select an entry by index label and column
print(df.loc[1,'Name'])
# Output: Bob

# Select an entry by position
print(df.iloc[1, 1])
# Output: 27