"""Dictionaries in Python are used to store data values in key:value pairs. A dictionary is a
collection that is ordered, mutable, and cannot have duplicate keys. If it has duplicate keys,
the last key-value pair will overwrite the previous ones. However, values can be duplicated.
Dictionaries are defined using curly braces {}, and key-value pairs are separated by commas. The
keys must be of an immutable data type (like strings, numbers, or tuples), while values can be of
any data type."""

# Creating a dictionary
Students = {"Name": ["Sameh", "Daniel", "John"], "Age": [25, 30, 22],
            "City": ["Cairo", "New York", "London"]}
print("\nOriginal Dictionary:", Students)
print("\nLength of Students Dictionary:", len(Students))
print("\nKeys in Students Dictionary:", Students.keys())
print("\nValues in Students Dictionary:", Students.values())
print("\nItems in Students Dictionary:", Students.items())
print("\nGet Age of Students:", Students.get("Age"))
print("\nGet Name of Students:", Students.get("Name"))
print("\nGet City of Students:", Students.get("City"))
print("\nGet non-existing key (default None):", Students.get("Country"))
print("\nAttempting to retrieve a non-existing key ('Country') with a default value:")
print("Result:", Students.get("Country", "Not Found"))

print("\nCheck if 'Name' key exists:", "Name" in Students)
print("\nCheck if 'Country' key exists:", "Country" in Students)

# NOTE:
# 1. Students["Name"].index("Sameh") finds the position of "Sameh" in the 'Name' list.
#    This returns an integer index (e.g., 0 if Sameh is the first element).
# 2. Students["Age"][...] uses that index to access the corresponding age in the 'Age' list.
# 3. Parentheses () are used with .index() because it is a method call.
# 4. Square brackets [] are used to retrieve the element at that position in the list.
# This allows us to find Sameh's age without hardcoding the index.
# This approach is dynamic and works even if the order of names changes in the list.
print("Sameh's Age:", Students["Age"][Students["Name"].index("Sameh")])
