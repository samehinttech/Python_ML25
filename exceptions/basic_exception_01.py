"""
This script demonstrates basic exception handling in Python using try and except block.
It repeatedly prompts the user until valid input is provided.
"""


def calculate_age():
    """Calculates and returns the user's age with proper exception handling."""
    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
            current_year = int(input("Enter the current year: "))

            # Validate the input years
            if birth_year > current_year:
                # If the birth year is greater than the current year, raise a ValueError
                raise ValueError("Birth year cannot be greater than current year.")
            # Calculate age
            age = current_year - birth_year
            # When valid input is provided, return the age
            return f"You are {age} years old."

        # Handle ValueError exceptions (e.g., non-integer input or logical errors)
        except ValueError as value_error:
            print(f"Error: {value_error}.... Please try again.\n")
        # Handle any other unexpected exceptions
        except Exception as exception_detail:
            print(f"An unexpected error occurred: {exception_detail}.... Please try again.\n")


# Call the function and display the result
print(calculate_age())