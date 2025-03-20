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
def student_scores(operation, **kwargs):
    try:
        if not kwargs:
            return ValueError("No student scores provided")
        if operation == "mean":
            return sum(kwargs.values()) / len(kwargs)
        elif operation == "best":
            return max(kwargs, key=kwargs.get)
        else:
            return f"Unsupported operation: {operation}"
    except (TypeError, ValueError):
        return "Invalid data was provided"
    
print(student_scores("mean", Anna=75, Marina=89, Denis=91))
print(student_scores("best", Anna=75, Marina=89, Denis=91))
print(student_scores("mean"))

# Task 8: Titleize, with String and List Operations
def titleize(sentence):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = sentence.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)

print(titleize("my name is anna, i am a developer."))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("alphabet", "ab"))

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif "qu" in word[:3]:
            qu_index = word.index("qu")
            result.append(word[qu_index + 2:] + word[:qu_index + 2] + "ay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(result)

print(pig_latin("quick"))
