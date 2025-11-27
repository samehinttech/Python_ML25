"""
This script demonstrates various mathematical functions using Python's built-in capabilities.
It includes examples of absolute value, rounding, exponentiation, square roots, and logarithms, excluding (Sine, Cosine, and Tangent).
More functions can be found in the math module documentation: https://docs.python.org/3/library/math.html
"""

# First, we need to import the math module to access the mathematical functions.
# Math is an object that we can access its operations and properties using dot notation.

import math

# Absolute Value
negative_number = -10
absolute_value = abs(negative_number)
print(f"The absolute value of {negative_number} is {absolute_value}")

# Rounding, be aware that round() rounds to the nearest even number, (1-4) rounds down,
# (5-9) rounds up.
number_to_round = 3.6
rounded_value = round(number_to_round)
print(f"{number_to_round} rounded is {rounded_value}")

# Exponentiation
base = 2
exponent = 3
power_value = pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_value}")
# Alternatively, you can use the ** operator for exponentiation
power_value_operator = base ** exponent
print(f"{base} raised to the power of {exponent} using ** operator is {power_value_operator}")

# Square Root
number_for_sqrt = 16
square_root = math.sqrt(number_for_sqrt)
print(f"The square root of {number_for_sqrt} is {square_root}")
# Alternatively, you can use exponentiation to find the square root
square_root_exponent = number_for_sqrt ** 0.5
print(f"The square root of {number_for_sqrt} using exponentiation is {square_root_exponent}")

# Logarithm
number_for_log = 100
log_value = math.log10(number_for_log)
print(f"The base-10 logarithm of {number_for_log} is {log_value}")
# Alternatively, you can use the natural logarithm (base e)
natural_log_value = math.log(number_for_log)
print(f"The natural logarithm of {number_for_log} is {natural_log_value}")
# You can also specify a different base for the logarithm
base_for_log = 10
log_value_base = math.log(number_for_log, base_for_log)
print(f"The logarithm of {number_for_log} with base {base_for_log} is {log_value_base}")

# Additional Mathematical Functions
# Ceiling: Rounds a number up to the nearest integer
number_for_ceil = 4.3
ceil_value = math.ceil(number_for_ceil)
print(f"The ceiling of {number_for_ceil} is {ceil_value}")

# Floor: Rounds a number down to the nearest integer
number_for_floor = 4.7
floor_value = math.floor(number_for_floor)
print(f"The floor of {number_for_floor} is {floor_value}")

# Factorial: Computes the factorial of a number Factorial is only defined for non-negative
# integers Rule: n! = n * (n-1) * (n-2) * ... * 1, and 0! = 1 by definition, where n is a
# non-negative integer.
number_for_factorial = 5
factorial_value = math.factorial(number_for_factorial)
print(f"The factorial of {number_for_factorial} is {factorial_value}")