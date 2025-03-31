# Task 2
import csv  
import traceback  

def read_employees(): 
    # Declare an empty dict. You'll add the key/value pairs to that. Declare also an empty list to store the rows.
    employees_dict = dict()
    employees_row = list()
        # You next read a csv file. 
        # Use a try block and a with statement, so that your code is robust and so that the file gets closed.
        # This ensures the file is automatically closed after the operation
    try:
        with open('csv/employees.csv', 'r') as file:  
            # Read ../csv/employees.csv using csv.reader(). (This csv file is used in a later lesson to populate a database.)
            reader = csv.reader(file)  
            # As you loop through the rows, store the first row in the dict using the key "fields". These are the column headers.
            header = next(reader)   # extracting only the first row and advancing the file reader to the next row
            employees_dict['fields'] = header  
            
            # Add all the other rows (not the first) to your rows list.
            for row in reader: 
                employees_row.append(row) 
            
            # Add the list of rows (this is a list of lists) to the dict, using the key "rows".
            employees_dict['rows'] = employees_row
            
            # The function should return the dict.
            return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list() 
        for trace in trace_back:  
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        
        print(f"An exception occurred. Exception type: {type(e).__name__}")
        message = str(e) 
        if message:
            print(f"Exception message: {message}") 
        print(f"Stack trace: {stack_trace}")  

# Add a line below the function that calls read_employees and stores the returned value in a global variable called employees. 
employees = read_employees()
# Then print out this value, to verify that the function works.
# print(employees)  


# Task 3: Find the Column Index

# Create a function called column_index.
# The input is a string. The function looks in employees["fields"]
# (an array of column headers) to find the index of the column header requested.
# The column_index function should return this index.
def column_index(column_name):
    return employees["fields"].index(column_name)

# Call the column_index function in your program, passing the parameter "employee_id".
# Store the column index you get back in a global variable called employee_id_column.
employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name

# Create a function called first_name.  
# It takes one argument, the row number.  
def first_name(row_number):
    
    # The function should retrieve the value of first_name from a row as stored in the employees dict.
    # You should first call your column_index function to find out what column index you want.
    first_name_column = column_index("first_name")
    
    # Then you go to the requested row as stored in the employees dict, 
    # and get the value at that index in the row.
    value = employees["rows"][row_number][first_name_column]
    
    # Return the value.
    return value

# Task 5: Find the Employee: a Function in a Function

# Create a function called employee_find.  
# This is passed one argument, an integer.  
# Just call it employee_id in your function declaration.
def employee_find(employee_id):
    
    # Inside the employee_find function create the following employee_match function:
    def employee_match(row):
        # This function is referencing the employee_id value that is passed to the employee_find function.  
        # It can access that value because the employee_match function is inside the employee_find function.
        # Note that we need to do type conversion here, because the CSV reader just returns strings as the values in the rows.
        # This inner function returns True if there is a match.  
        # We are using the employee_id_column global value you set in Task 3.
        return int(row[employee_id_column]) == employee_id

    # Now, still within the employee_find function, call the filter() function.   
    # The filter() function needs to know how to filter, and the employee_match function provides that information.  
    # The filter() function calls employee_match once per row, saying, Do we want this one?  
    # When the filter function completes, we need to do type conversion to convert the result to a list.
    matches = list(filter(employee_match, employees["rows"]))

    # The employee_find function then returns the matches.
    return matches

# Task 6: Find the Employee with a Lambda

# Create a function employee_find_2.
# This function does exactly what employee_find does -- but it uses a lambda.
def employee_find_2(employee_id):
    # Use the filter() function with a lambda.
    # The lambda takes a row as input and checks if the "employee_id" in that row matches the provided employee_id.
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    # Return the matches as a list.
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda

# Create a function sort_by_last_name.
# This function takes no parameters. You sort the rows you have stored in the dict.
def sort_by_last_name():
    # Within the function, you call employees["rows"].sort().
    # This sorts the list of rows in place.
    
    # But, you need to pass to the list.sort() method a keyword argument called key.
    # Set that keyword parameter equal to a lambda.
    # The lambda is passed the row, and the expression after the colon gives the value from the row to be used in the sort.
    # You might want to use your column_index function for last_name so you know which value from the row should be given in the lambda expression.
    # Remember that the sort() method sorts the list in place and does not return the sorted list.
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])

    # The sort_by_last_name function returns the sorted list of rows.
    return employees["rows"]

# sort_by_last_name()
# print(employees)  

# Task 8: Create a dict for an Employee

# Create a function called employee_dict.  
# It is passed a row from the employees dict (not a row number).  
def employee_dict(row):
    # It returns a dict.
    # The keys in the dict are the column headers from employees["fields"].
    # The values in the dict are the corresponding values from the row.

    # Do not include the employee_id in the dict. You skip that field for now.
    # Use zip() to simplify matching headers to values.
    employee = {
        key: value for key, value in zip(employees["fields"], row) 
        if key != "employee_id"
    }
    
    # Return the resulting dict for the employee.
    return employee

# result = employee_dict(employees["rows"][0])
# print(result)  # Print the resulting dictionary for the first row in employees["rows"]

# Task 9: A dict of dicts, for All Employees

# Create a function called all_employees_dict.
def all_employees_dict():
    # The keys in the dict are the employee_id values from the rows in the employees dict.
    # For each key, the value is the employee dict created for that row. 
    # (Use the employee_dict function you created in Task 8.)
    all_employees = {
        row[employee_id_column]: employee_dict(row) for row in employees["rows"]
    }

    # The function should return the resulting dict of dicts.
    return all_employees

# all_employees = all_employees_dict()
# print(all_employees)  # Print the resulting dict of dicts for all employees.

# Task 10: Use the os Module
import os

# Create a function get_this_value().
# This function takes no parameters and returns the value of the environment variable THISVALUE.
def get_this_value():
    # Access the environment variable THISVALUE using os.getenv().
    return os.getenv("THISVALUE")

# print(get_this_value()) 

# Task 11: Creating Your Own Module
import custom_module

# Create a function called set_that_secret.
# It should accept one parameter, which is the new secret to be set.
def set_that_secret(new_secret):
    # It should call custom_module.set_secret(), passing the parameter,
    # so as to set the secret in custom_module.
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
# print(custom_module.secret)  

# Task 12: Read minutes1.csv and minutes2.csv

# Create a function called read_minutes.
# This function takes no parameters.
def read_minutes():
    # Helper function to read a CSV file and convert its rows to tuples.
    def read_csv_to_dict(filepath):
        data = {"fields": [], "rows": []}
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            # Store the first row as fields.
            data["fields"] = next(reader)
            # Store the rest of the rows as tuples in the rows list.
            data["rows"] = [tuple(row) for row in reader]
        return data

    # It creates two dicts, minutes1 and minutes2, 
    # by reading /csv/minutes1.csv and /csv/minutes2.csv.
    minutes1 = read_csv_to_dict("csv/minutes1.csv")
    minutes2 = read_csv_to_dict("csv/minutes2.csv")

    # The function should return both minutes1 and minutes2.
    return minutes1, minutes2

# Store the values from the values it returns in the global variables minutes1 and minutes2.
minutes1, minutes2 = read_minutes()

# print("Minutes 1:")
# print(minutes1)
# print("\nMinutes 2:")
# print(minutes2)

# Task 13: Create minutes_set

# Create a function called create_minutes_set.  
# This function takes no parameters.
def create_minutes_set():
    # It creates two sets from the rows of minutes1 and minutes2 dicts.
    # (This is just type conversion. However, to make it work, each row has to be hashable!)
    # (Sets only support hashable elements. Lists aren't hashable, so that is why you stored the rows as tuples in Task 10.)
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    # Combine the members of both sets into one single set.
    # (This operation is called a union.)
    combined_set = set1.union(set2)

    # The function returns the resulting set.
    return combined_set


minutes_set = create_minutes_set()

# print("Minutes Set:")
# print(minutes_set)

# Task 14: Convert to datetime

# Add a statement, from datetime import datetime, to your program.
from datetime import datetime

# Create a function called create_minutes_list.
# This function takes no parameters.
def create_minutes_list():
    # Create a list from the minutes_set.
    # This is just type conversion.
    minutes_list = list(minutes_set)

    # Use the map() function to convert each element of the list.
    # At present, each element is a list of strings, where the first element of that list
    # is the name of the recorder and the second element is the date when they recorded.

    # The map() should convert each of these into a tuple.
    # The first element of the tuple is the name (unchanged).
    # The second element of the tuple is the date string converted to a datetime object.
    # Use the lambda to define this conversion inline.
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    # The function should return the resulting list.
    return minutes_list

minutes_list = create_minutes_list()

# print("Minutes List:")
# print(minutes_list)

# Task 15: Write Out Sorted List

# Create a function called write_sorted_list.  
# This function takes no parameters.
def write_sorted_list():
    # Step 1: Sort minutes_list in ascending order of datetime.
    # Use the sorted() function to sort minutes_list in place based on the second element of the tuple (the datetime).
    global minutes_list  # Ensure we're using the global minutes_list variable.
    minutes_list.sort(key=lambda x: x[1])

    # Step 2: Call map again to convert the list.
    # For each tuple, create a new tuple where:
    # The first element is the name (unchanged).
    # The second element is the datetime converted back to a string using datetime.strftime().
    converted_list = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    )

    # Step 3: Open a file called ./minutes.csv.
    # Use a csv.writer to write out the resulting sorted data.
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # The first row you write should be the value of fields from minutes1 dict.
        writer.writerow(minutes1["fields"])

        # The subsequent rows should be the elements from minutes_list.
        writer.writerows(converted_list)

    # The function should return the converted list.
    return converted_list

result = write_sorted_list()
# print("Converted List:")
# print(result)
