"""
This script demonstrates basic input and output operations in Python.
It includes examples of printing to the console and reading user input.
"""


# Main function to encapsulate the code instead of running it at the top level We can use None as
# the return type since this function does not return any value " def main() -> None: "
def main():
    # Output: Print a welcome message to the console
    print("Welcome to the Input/Output Practice")

    # Input: Prompt the user for their name
    name = input("Please enter your name: ")

    # Output: Greet the user with their name
    # Using an f-string for formatted output
    print(f"Hello, {name}! Nice to meet you.")


# Call the main function if this script is executed.
# This is a common Python idiom for making code only run when the script is executed directly
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()