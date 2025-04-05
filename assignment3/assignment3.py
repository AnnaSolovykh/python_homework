import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# 1. Create a DataFrame from a dictionary:
#    * Use a dictionary containing the following data:
#       * Name: ['Alice', 'Bob', 'Charlie']
#       * Age: [25, 30, 35]
#       * City: ['New York', 'Los Angeles', 'Chicago']
#    * Convert the dictionary into a DataFrame using Pandas.
#    * Print the DataFrame to verify its creation.
#    * save the DataFrame in a variable called task1_data_frame and run the tests.


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

# 2. Add a new column:
#    * Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
#    * Add a column called Salary with values [70000, 80000, 90000].
#    * Print the new DataFrame and run the tests.

task1_with_salary= task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

# 3. Modify an existing column:
#    * Make a copy of task1_with_salary in a variable named task1_older
#    * Increment the Age column by 1 for each entry.
#    * Print the modified DataFrame to verify the changes and run the tests.

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1

print(task1_older)

# 4. Save the DataFrame as a CSV file:
#    * Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
#    * Look at the contents of the CSV file to see how it's formatted.
#    * Run the tests.

task1_older.to_csv('employees.csv', index=False)
print("Saved to 'employees.csv'")
