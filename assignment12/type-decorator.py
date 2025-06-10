"""
Assignment 12 - Task 2: A Decorator that Takes an Argument
"""

import functools

# Task 2.2: A decorator factory takes type parameter and creates customized decorator
def type_converter(type_of_output):
   # Returns actual decorator function that will be applied to target function
   def decorator(func):
       # Preserve original function's metadata 
       @functools.wraps(func)
       # Wrapper function that replaces original function
       def wrapper(*args, **kwargs):
           # Call original function with same arguments, store result
           x = func(*args, **kwargs)
           # Convert result to specified type and return it
           return type_of_output(x)
       
       return wrapper
   return decorator

# Task 2.3 type_converter(str) creates decorator that converts return value to string
@type_converter(str)
def return_int():
   return 5

# Task 2.4: type_converter(int) creates decorator that converts return value to int
@type_converter(int)
def return_string():
   return "not a number"

# Task 2.5: Mainline code to test the decorated functions
if __name__ == "__main__":
   print("Testing type converter decorator...")
   
   # Test return_int() - should return "5" (string) instead of 5 (int)
   y = return_int()
   print(f"return_int() result: {y}")
   print(f"Type: {type(y).__name__}")  # Should print "str"
   
   # Test return_string() - should fail because can't convert "not a number" to int
   try:
       y = return_string()
       print("shouldn't get here!")
   except ValueError:
       print("can't convert that string to an integer!")  # This should happen