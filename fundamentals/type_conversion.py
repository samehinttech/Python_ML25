"""This script demonstrates type conversion in Python, including implicit and explicit
conversions between different data types. It covers conversions between integers, floats,
strings, and booleans."""
# Using simple variable declarations and assignments

birth_year = input("Enter your birth year: ")
# age = 2025 - birth_year # This will raise an error because birth_year is a string
age = 2025 - int(birth_year)  # Explicit conversion from string to integer
print(f"\nYour age is: {age} years old")

# Implicit conversion (Python automatically converts types)
num1 = 10      # Integer
num2 = 5.5     # Float
result = num1 + num2  # num1 is implicitly converted to float
print(f"\nResult of adding integer and float: {result}")

# Explicit conversion (type casting)
# Integer to Float
int_value = 10
float_value = float(int_value)
print(f"\nInteger to Float: {float_value}")

# String to Integer
str_value = "20"
int_value = int(str_value)
print(f"\nString to Integer: {int_value}")

# Boolean to Integer
bool_value = True
int_value = int(bool_value)  # True becomes 1, False becomes 0
print(f"\nBoolean to Integer: {int_value}")