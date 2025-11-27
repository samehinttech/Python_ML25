"""
Script to demonstrate the use of else and finally clauses in exception handling.
"""


def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
    else:
        print(f"\nThe result is: {result}")
    finally:
        print("\nSee you later!")


divide_numbers()