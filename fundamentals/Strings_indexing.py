"""
This script demonstrates string indexing in Python.
It covers positive and negative indexing, as well as slicing.
It also includes examples of string immutability and how to work around it.
"""

# Define a sample string
sample_string = "Hello, World!"
print(f"Sample String: {sample_string}")

# Positive Indexing
first_char = sample_string[0]  # First character

fifth_char = sample_string[4]  # Fifth character
print(f"Positive Indexing: First character: '{first_char}', Fifth character: '{fifth_char}'")

# Negative Indexing
last_char = sample_string[-1]  # Last character
second_last_char = sample_string[-2]  # Second last character
print(f"Negative Indexing: Last character: '{last_char}', Second last character: '{second_last_char}'")

# Slicing
substring = sample_string[0:5]  # Characters from index 0 to 4
print(f"Slicing: Substring from index 0 to 4: '{substring}'")

# Slicing with a step value
step_slice = sample_string[0:12:2]
# Every second character from index 0 to 11 as the end index is exclusive
print(f"Slicing with step: Every second character from index 0 to 11: '{step_slice}'")


# More indexing examples
from_start_to_end = sample_string[:]
print(f"Slicing from start to end: '{from_start_to_end}'")


# String Immutability
# Note: Strings in Python are immutable, meaning they cannot be changed after they are created.
# To modify a string, you need to create a new string.
# Creating a new string to replace "World" with "Universe",
# it keeps all characters from index 0 to 6 and adds "Universe!"
modified_string = sample_string[:7] + "Universe!"
print(f"String Immutability: Modified string: '{modified_string}'")

# Reversing a String using slicing
# [start:stop:step] with a step of -1 reverses the string
# start: 0 (beginning of the string)
# stop: None (goes until the end of the string)
# step: if step is positive(slicing moves forward(left to right)),
# if step is negative(slicing moves backward(right to left))
# step: -1 (moves backwards through the string), if step is negative,
# start should be greater than stop to get a non-empty result

reversed_string = sample_string[::-1]  # Reverses the string
print(f"Reversed String: '{reversed_string}'")

# Length of the string
# Note: The len() function returns the number of characters in the string,
# including spaces and punctuation.
string_length = len(sample_string)
print(f"Length of the string: {string_length}")