"""
A guessing game where the user has to guess a predefined number.
"""
from idlelib.configdialog import is_int

predefined_number = 25
guess_limit = 3
attempts = 0
print("Welcome to the Guessing Game!")
print(f"You have {guess_limit} attempts to guess the correct number between 1 and 50.")
print("Type 'exit' to quit_game the game.")

# type exit to quit_game the game using while loop
while attempts < guess_limit:
    user_guess = input("Enter your guess: ")

    # To Allow user to exit the game
    if user_guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break  # to break the loop and exit the game
        # Check if the input is a valid integer
    elif not is_int(user_guess):  # using is_int() function
        print("Invalid input. Please enter a valid integer.")
        continue
    else:
        user_guess = int(user_guess)  # Cast the user input to an integer

        # Increment the attempts counter
        attempts += 1
        if user_guess < 1 or user_guess > 50:
            print("Please guess a number between 1 and 50.")
        elif user_guess < predefined_number:
            print("Too low! Try again.")
        elif user_guess > predefined_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number "
                  f"{predefined_number} in {attempts} attempts.")
            break
else:
    print(f"Sorry, you've used all your attempts. The correct number was {predefined_number}.")