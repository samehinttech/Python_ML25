"""
This script is extended from functions_01.py and includes examples of:
- Functions with parameters
- Functions with return values
- Functions with default parameters
- Functions with variable-length arguments
- Functions with **kwargs for named arguments
- Functions with keyword arguments
- Lambda functions
- Docstrings for documentation
- Type hints for better code clarity

Important: When dealing with positional and keyword arguments, positional arguments must always
come before keyword arguments in function calls. Important: Default parameters must always come
after non-default parameters in function definitions. Example: def func(a, b=2) is valid,
but def func(a=2, b) is not."""


# Function with parameters and return value
def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


print(f"\nSum of 3 and 5 is: {add(3, 5)}")  # Output: 8


# Function with default parameters
def sum_of_integers(a: int, b: int = 10) -> int:
    """Returns the sum of two integers, with a default value for the second parameter."""
    return a + b


print(f"\nSum of 5 and default 10 is: {sum_of_integers(5)}")  # Output: 15
print(f"\nSum of 5 and 20 is: {sum_of_integers(5, 20)}")  # Output: 25


# Function with variable-length arguments
def multiply(*args: int) -> int:
    """Returns the product of all provided integers."""
    product = 1
    for num in args:
        product *= num
    return product


print(f"\nProduct of 2, 3, and 4 is: {multiply(2, 3, 4)}")  # Output: 24
print(f"\nProduct of 5 and 6 is: {multiply(5, 6)}")  # Output: 30


# Function with keyword arguments
def greet(name: str, greeting: str = "Hello") -> str:
    """Returns a greeting message."""
    return f"{greeting}, {name}!"


print(f"\nGreeting: {greet('Sameh')}")  # Output: Hello, Sameh!
print(f"\nGreeting: {greet('Sameh', greeting='Bye')}")  # Output: Bye, Sameh!


# Lambda function
def square(x: int) -> int:
    """Returns the square of an integer using an inline lambda function."""
    return (lambda num: num * num)(x)


print(f"\nSquare of 6 is: {square(6)}")  # Output: 36


# Function with **kwargs to handle named arguments
def display_info(**info):
    """Displays key-value pairs passed as keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")


print("\nDisplaying info:")
display_info(name="Sameh", age=20, city="New York")
# Output:
# name: Sameh
# age: 20
# city: New York
