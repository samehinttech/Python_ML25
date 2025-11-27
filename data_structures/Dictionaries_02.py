"""
Iteration through a dictionary using a for loop and print each key-value pair.
"""

# Define a dictionary
employees = {"Mark": "Manager", "Sally": "Salesperson", "Jack": "Clerk"}

for key, value in employees.items():
    print(f"{key} is a {value}")

# Using enumerating to get index and key-value pairs
for index, (key, value) in enumerate(employees.items()):
    print(f"{index}: {key} is a {value}")

# We can also use a while loop to iterate through the dictionary. However, this is more time
# complex and less efficient than using a for loop.
keys = list(employees.keys())
index = 0
while index < len(keys):
    key = keys[index]
    value = employees[key]
    print(f"{key} is a {value}")
    index += 1
