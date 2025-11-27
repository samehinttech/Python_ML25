"""This script demonstrates basic list operations in Python, including creation, indexing,
slicing, and modification of lists."""

# Example 1: Creating a list and accessing its elements.
fruits_basket = ["apple", "banana", "cherry", "dates"]
print(f"\nExample 1")
print(f"Fruits Basket: {fruits_basket}")

# Accessing elements by index
# [start index:end index]
# [inclusive:exclusive]
# [start index:] means from start index to the end of the list
# [:end index] means from the start of the list to the end index (exclusive)
# [-1] means the last element of the list
# [-2] means the second last element of the list and so on...
# [::-1] means the list in reverse order
# [start index:end index:step] means from start index to end index with a step of 'step'
# noinspection PyTypeHints
print(f"First fruit: {fruits_basket[0]}")  # Output: apple
# noinspection PyTypeHints
print(f"Last fruit: {fruits_basket[-1]}")  # Output: dates, which is the first fruit from the end
# of the list


# Example 2: Slicing a list to get a sublist.
print(f"\nExample 2")
# noinspection PyTypeHints
my_favorite_fruits = fruits_basket[1:3]  # Slicing from index 1 to 2 (3 is exclusive)
print(f"My favorite fruits: {my_favorite_fruits}")  # Output: ['banana', 'cherry']

# Example 3: Modifying a list by adding and removing elements.
print(f"\nExample 3")
# Adding elements
# append() adds an element at the end of the list
# insert(index, value) adds an element at the specified index
fruits_basket.append("elderberry")  # Adding at the end
fruits_basket.insert(1, "blueberry")  # Inserting at index
print(f"Fruits Basket after additions: {fruits_basket}")
# Output: ['apple', 'blueberry', 'banana', 'cherry', 'dates', 'elderberry']

# Removing elements remove() removes the first occurrence of the value pop() works as a stack in
# java, removing the last item by default or the item at the specified index, LIFO rule pop(
# index) removes the item at the specified index, FIFO rule as queue in java
fruits_basket.remove("banana")  # Remove by value
print(f"Fruits Basket after removals: {fruits_basket}")
popped_fruit = fruits_basket.pop()
print(f"Popped fruit: {popped_fruit}")
