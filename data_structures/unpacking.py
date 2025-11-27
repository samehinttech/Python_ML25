"""
Unpacking is a powerful feature in Python that allows you to assign values from iterables
(like lists, tuples, or dictionaries) to multiple variables in a single statement.
This can make code cleaner and more readable.
"""

# Example 1: Unpacking a tuple
# (m, b) for the line equation y = mx + b in the slope-intercept form
coefficients = (1, 2)

# Unpack the tuple
m, b = coefficients

# Display the unpacked values
print("Slope (m):", m)
print("Y-Intercept (b):", b)

# print the equation of the line using the unpacked values, for (m), if it is 1, we don't need to
# print it
if m == 1:
    print(f"Equation of the line: y = x + {b}")
elif m == -1:
    print(f"Equation of the line: y = -x + {b}")
else:
    print(f"Equation of the line: y = {m}x + {b}")
