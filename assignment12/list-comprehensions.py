"""
Task 3: List Comprehensions
"""

import pandas as pd

# Task 3.1: Read CSV file into DataFrame
df = pd.read_csv("../csv/employees.csv")

print("Employee DataFrame:")
print(df.head())

# Task 3.2: Iterate through DataFrame rows and combine first_name + last_name
employee_names = [f"{row['first_name']} {row['last_name']}" 
                  for _, row in df.iterrows()]

print("\nAll employee names:")
print(employee_names)

# Task 3.3: Create new list from previous list, include only names with letter "e"
names_with_e = [name for name in employee_names if "e" in name.lower()]

print(f"\nNames containing letter 'e' ({len(names_with_e)} employees):")
print(names_with_e)
