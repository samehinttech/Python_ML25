"""
This script demonstrates the use of for loops in Python.
It includes examples of iterating over strings and range of a number sequence.
"""

# Example 1: Iterating over each character in a string
name = "Sameh"
print(f"Example 1: Iterating over each character in a string")
for char in name:
    print(char)  # Output each character in the string "Sameh" each in a new line

# Example 2: Using the range function to iterate over a sequence of numbers
print(f"\nExample 2: Using the range function to iterate over a sequence of numbers")
for i in range(5):  # This will iterate from 0 to 4
    print(i)  # Output numbers from 0 to 4, each in a new line

# Example 3: Using range with a start and end value
print(f"\nExample 3: Using range with a start and end value")
for i in range(1, 6):  # This will iterate from 1 to 5
    print(i)  # Output numbers from 1 to 5, each in a new line

# Example 4: Using range with a step value
print(f"\nExample 4: Using range with a step value")
for i in range(0, 10, 2):  # This will iterate from
    print(i)  # Output even numbers from 0 to 8, each in a new line

# Example 5: Nested for loops This is just a simple representation of a 2D array using nested
# loops to get the positions rather than actual values
print(f"\nExample 5: Nested for loops")
for i in range(3):  # Outer loop for rows
    for j in range(3):  # Inner loop for columns
        print(f"Element at ({i}, {j})")