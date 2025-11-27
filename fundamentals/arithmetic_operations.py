"""
This script demonstrates basic arithmetic operations in Python.
It covers addition, subtraction, multiplication, division, and modulus. As well as the operator precedence.

Operator Precedence:
1. Parentheses
2. Exponents
3. Negative and positive arguments
4. Multiplication, Division, Floor division, Modulus, and @ (from left to right)
5. Addition and Subtraction (from left to right)
6. Equality (==, =, >, <, >=, <=)
7. Logical NOT
8. Logical AND (and)
9. Logical OR (or)
"""

# Addition
a = 10
b = 5
addition = a + b
print(f"Addition: {a} + {b} = {addition}")

# Subtraction
subtraction = a - b
print(f"Subtraction: {a} - {b} = {subtraction}")

# Multiplication
multiplication = a * b
print(f"Multiplication: {a} * {b} = {multiplication}")

# Division
division = a / b
print(f"Division: {a} / {b} = {division}")

# Floor Division
floor_division = a // b
print(
    f"Floor Division: {a} // {b} = {floor_division}")  # Note: Floor division returns the largest integer less than or equal to the division result.

# Modulus
modulus = a % b
print(f"Modulus: {a} % {b} = {modulus}")  # Note: Modulus returns the remainder of the division.

# Exponentiation
exponentiation = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation}")

# Demonstrating operator precedence
result = a + b * 2 - (
        a / b) ** 2  # Parentheses first, then exponentiation, then multiplication, then addition
# and subtraction from left to right
print(f"Operator Precedence Result: {result}")

# Augmented Assignment Operators Note: Augmented assignment operators modify the variable in
# place and can improve code readability. Note: In Python, the division operator (/) always
# returns a float, even if the division is exact. For integer division, use the floor division
# operator (//).
x = 10
print(f"Initial x: {x}")
x += 5  # Equivalent to x = x + 5
print(f"After x += 5: {x}")
x -= 3  # Equivalent to x = x - 3
print(f"After x -= 3: {x}")
x *= 2  # Equivalent to x = x * 2
print(f"After x *= 2: {x}")
x /= 4  # Equivalent to x = x / 4
print(f"After x /= 4: {x}")
x //= 2  # Equivalent to x = x // 2
print(f"After x //= 2: {x}")
x %= 3  # Equivalent to x = x % 3
print(f"After x %= 3: {x}")
x **= 3  # Equivalent to x = x ** 3
print(f"After x **= 3: {x}")