# Task 1: Hello
def hello():
    return "Hello!"

print(hello())

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

print(greet("Anna"))

# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b 
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(2, 5))
print(calc(5, 2, "substsubtractract"))
print(calc("10", 5, "modulo"))
print(calc(4, 0, "divide"))

# Task 4: Data Type Conversion
def data_type_conversion(value, target_type):
    try:
        match target_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {target_type}."

print(data_type_conversion("90", "int"))

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError, ZeroDivisionError):
        return "Invalid data was provided."

print(grade(76, 100, 80))

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("python", 5))
# Task 7: Student Scores, Using **kwargs

# Task 8: Titleize, with String and List Operations

# Task 9: Hangman, with more String Operations

# Task 10: Pig Latin, Another String Manipulation Exercise