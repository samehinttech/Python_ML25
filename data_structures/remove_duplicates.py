"""
This program removes duplicate elements from a list while preserving the original order of elements.
"""
numbers = [1, 2, 3, 4, 5, 3, 2, 1]
print(f"\nOriginal list: {numbers}")

# Method 1: Using a loop and a new list to store unique elements
non_duplicated_numbers = []
for num in numbers:
    if num not in non_duplicated_numbers:
        non_duplicated_numbers.append(num)
print(f"List after removing duplicates (method 1): {non_duplicated_numbers}")

# Method 2: Using a set to track seen elements and a list comprehension
seen = set()
non_duplicated_numbers = [x for x in numbers if not (x in seen or seen.add(x))]
print(f"List after removing duplicates (method 2): {non_duplicated_numbers}")

# Method 3: Using dict.fromkeys() to remove duplicates while preserving order (Python 3.7+)
non_duplicated_numbers = list(dict.fromkeys(numbers))
print(f"List after removing duplicates (method 3): {non_duplicated_numbers}")