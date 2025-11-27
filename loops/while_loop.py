"""
This script demonstrates the use of while loops in Python.
"""

# Example 1: Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop
print("Finished counting to 5.")

# Example 2: While loop with a break statement
number = 0
while True:
    print("Number is:", number)
    number += 1
    if number >= 3:
        print("Breaking the loop as number reached", number)
        break  # Exit the loop when the number reaches 3
print("Exited the loop.")

# Example 3: While loop with a continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the loop when i is 3
    print("Current number is:", i)
print("Finished processing numbers.")

# Example 4: While loop with an else clause
j = 0
while j < 3:
    print("j is:", j)
    j += 1
else:
    print("j has reached the limit of 3.")
print("Loop with else clause completed.")

# Example 5: Nested while loops
outer = 0
while outer < 2:
    inner = 0
    while inner < 2:
        print("Outer:", outer, "Inner:", inner)
        inner += 1
    outer += 1
print("Nested loops completed.")