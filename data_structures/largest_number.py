"""
A program to practice list manipulation by finding the largest number in a list.
 Assume the list contains [5, 3, 8, 6, 2] and the expected output is 8.
"""
numbers = [5, 3, 8, 6, 2]
largest_number = numbers[0]   # Assume the first number is the largest initially
for num in numbers:           # Iterate through each number in the list
    if num > largest_number:  # Compare with the current largest number
        largest_number = num  # Update largest_number if the current number is larger
print(f"Largest number in the list is: {largest_number}")