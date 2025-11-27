"""
This script demonstrates the use of 2D lists (lists of lists) in Python.
Note that modifying a 2D list is similar to modifying a regular list.
"""
# Example 1: Creating a 2D list (list of lists) and accessing its elements.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nExample 1")
print(f"Matrix: {matrix}")
# Accessing elements by row and column index
# matrix[row index][column index]
print(f"Element at row 1, column 2: {matrix[1][2]}")  # Output: 6

# We can also iterate through the 2D list using nested loops
print("\nMatrix elements with for loop iteration:")
for row in matrix:
    for element in row:
        # Print elements in a single line with space separation
        print(element, end=" ")
        # For a new line after each row
    print()
