"""Like any programming language, Python has variables that are used to store data in memory.
This module to learn about variables, including how to declare them, assign values,
and use different data types.
# Simple variable declaration and assignment In Python, you don't need to explicitly declare the
# type of variable. The type is inferred from the value assigned to it. However, you can use type
# hints for better code readability and type checking. By default, Python uses dynamic typing,
# meaning you can change the type of variable by reassigning it. Important: Python is
# case-sensitive, so 'Variable' and 'variable' would be considered different identifiers.
# Important: Variable names should start with a letter (a-z, A-Z) or an underscore (_), followed
# by letters, digits (0-9), or underscores. Important: Variable names cannot be a reserved
# keyword in Python (like def, class, if, else, etc.) Important: Python uses snake_case for
# variable names by convention (e.g., my_variable_name). Important: Python interpreters read the
# code from top to bottom, so variables must be defined before they are used. Here I used {type(
# variable)} to show the type of each variable. Integer variable
"""
age: int = 25
print(f"Age: {age} (Type: {type(age)})")

# Float variable, with a decimal point
height: float = 175.5  # in cm
print(f"Height: {height} cm (Type: {type(height)})")

# String variable
name: str = "Sameh"
print(f"Name: {name} (Type: {type(name)})")

# Boolean variable
is_student: bool = True  # same as is_student = True, without type hinting
print(f"Is Student: {is_student} (Type: {type(is_student)})")

# Multiple assignments
x, y, z = 1, 2.5, "Hello"
print(f"x: {x}, y: {y}, z: {z}")

# Constants (by convention, using uppercase letters)
PI: float = 3.14159
print(f"PI: {PI} (Type: {type(PI)})")

# Variable reassignment
age = 26
print(f"updated Age: {age}")
