"""
Tuples are similar to lists, but they are immutable (cannot be modified).
They are defined using parentheses () instead of square brackets [].
In other words, once a tuple is created, its elements cannot be changed, added, or removed.

Definition: Tuple are immutable sequences, typically used to store collections of heterogeneous
data. Note that single element tuples need a trailing comma, e.g., (1,). Without the comma,
it is just an integer in parentheses."""

# Creating a tuple
my_tuple = (1, 2, 3, "hello", True)
print("\nOriginal Tuple:", my_tuple)

# Accessing elements in a tuple
print("\nFirst Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])
print("Slicing Tuple:", my_tuple[1:4])

# Tuples are immutable, so the following line would raise an error if uncommented
# my_tuple[0] = 10  # This will raise a TypeError
# However, you can concatenate tuples to create a new one
new_tuple = my_tuple + (4, 5, 6)
print("\nConcatenated Tuple:", new_tuple)

# You can also repeat tuples
repeated_tuple = my_tuple * 2
print("\nRepeated Tuple:", repeated_tuple)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("\nUnpacked Values:", a, b, c, d, e)

# You can also use the asterisk (*) to unpack remaining elements
first, *middle, last = new_tuple
print("\nFirst element:", first)
print("Middle elements:", middle)
print("Last element:", last)

# Tuple methods
# Note: Tuples have only two built-in methods: count() and index()
print("\nCount of 1 in my_tuple:", my_tuple.count(1))
print("Index of 'hello' in my_tuple:", my_tuple.index("hello"))

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5, (6, 7)))
print("\nNested Tuple:", nested_tuple)
print("Accessing Nested Element:", nested_tuple[2][2][1])  # Output: 7
