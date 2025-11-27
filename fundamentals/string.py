"""This script demonstrates how to use strings in Python, including declaration, assignment,
and various string operations. It covers string concatenation, repetition, indexing, slicing,
and common string methods."""
# Simple string declaration and assignment
greeting: str = "Hello"
name: str = "Sameh"
print(f"{greeting}, {name}!")  # Output: Hello, Sameh!

# String concatenation
full_greeting: str = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Sameh!

# String repetition
repeat_greeting: str = greeting * 3
print(repeat_greeting)  # Output: HelloHelloHello

# String indexing (accessing individual characters)
first_char: str = name[0]  # 'S' index starts at 0
last_char: str = name[-1]  # 'h' negative index starts from the end
print(f"First character: {first_char}, Last character: {last_char}")

# String slicing (extracting a substring)
substring: str = name[1:4]  # 'ame' from index 1 to 3, note that the end index is exclusive
print(f"Substring: {substring}")

# Common string methods
upper_name: str = name.upper()  # Convert to uppercase
lower_name: str = name.lower()  # Convert to lowercase
capitalized_name: str = name.capitalize()  # Capitalize the first letter
replaced_name: str = name.replace("a", "@")  # Replace 'a'
print(f"Upper: {upper_name}, Lower: {lower_name}, Capitalized: {capitalized_name}, Replaced: {replaced_name}")

# String length
name_length: int = len(name)  # Get the length of the string
print(f"Length of name: {name_length}")

# Check if a substring exists
contains_substring: bool = "am" in name  # True if 'am' is in 'Sameh'
print(f"Contains 'am': {contains_substring}")

# Find the position of a substring
position: int = name.find("me")  # Returns the starting index of 'me',
print(f"Position of 'me': {position}")  # (index starts at 0), returns -1 if not found, Here 'me'
# starts at index 2

# Title case
title_name: str = "sameh ahmed".title()  # Converts to a title case
print(f"Title Case: {title_name}")  # Output: Sameh Ahmed

# String formatting using f-strings
age: int = 25
formatted_string: str = f"{name} is {age} years old."  # {} are placeholders for variables
print(formatted_string)  # Output: Sameh is 25 years old.

# Note: Python strings are immutable, meaning once a string is created, it cannot be changed. Any
# operation that modifies a string will create a new string. For example, the replace method
# above does not change the original string 'name', it returns a new string with the replacement.

# You can use triple quotes for multi-line strings
multi_line_string: str = """This is my Python learning repository.
It contains various examples and exercises to game_instructions me understand Python programming better.
Happy Coding!, Sameh
"""
print(multi_line_string)