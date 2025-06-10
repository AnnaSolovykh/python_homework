"""
Task 1: Writing and Testing a Decorator
"""

import logging
import functools

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Task 1.2: Declare a decorator that logs function calls including name, parameters, and return value.
def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # If there are positional args - make a list, if not - "none"
        pos_params = list(args) if args else "none"
        
        # If there are keyword args - make a dict, if not - "none"
        kw_params = dict(kwargs) if kwargs else "none"
        
        # Call original function with same arguments, save the result
        result = func(*args, **kwargs)
        
        # Format log string with function name, parameters and return value
        log_message = (f"function: {func.__name__} "
                      f"positional parameters: {pos_params} "
                      f"keyword parameters: {kw_params} "
                      f"return: {result}")
        
        logger.log(logging.INFO, log_message)
        
        return result
    # Return wrapper function that will replace the original function
    return wrapper


# Task 1.3: Function that takes no parameters and returns nothing
@logger_decorator
def hello_world():
    print("Hello, World!")
    return None


# Task 1.4: Function that takes variable number of positional arguments and returns True
@logger_decorator
def variable_positional(*args):
    return True


# Task 1.5: Function that takes no positional arguments and variable keyword arguments, returns logger_decorator
@logger_decorator
def variable_keyword(**kwargs):
    return logger_decorator


# Task 1.6: Mainline code to test the decorated functions
if __name__ == "__main__":
    print("Testing decorated functions...")
    
    print("\n1. Testing hello_world() - no parameters:")
    hello_world()
    
    print("\n2. Testing variable_positional() - with positional arguments:")
    variable_positional(1, 2, 3, "test")
    
    print("\n3. Testing variable_keyword() - with keyword arguments:")
    variable_keyword(name="John", age=25, city="New York")
    
    print("\n4. Additional test - variable_positional with no args:")
    variable_positional()
    
    print("\n5. Additional test - variable_keyword with no kwargs:")
    variable_keyword()
    
    print("\nCheck './decorator.log' file for logged function calls.")