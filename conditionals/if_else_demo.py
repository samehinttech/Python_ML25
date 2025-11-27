"""
This script demonstrates conditional statements in Python using if, elif, and else.
I will also use more than just if statements to practice logical operators.
"""

# Define a variable
good_weather = True
is_raining = False
temperature = 10  # Temperature in degrees Celsius


# Conditional statements, Here you can change the values of good_weather,
# is_raining, and temperature to see different outputs.
if good_weather:
    print("It's a nice day! Let's go for a walk.")
elif is_raining:
    print("It's raining. Better stay indoors.")
elif temperature < 0:
    print("It's freezing outside! Wear a warm coat.")
else:
    print("The weather is okay. Maybe go for a short walk.")


# Another example with nested conditions
"""Here the first condition checks if the weather is good, If true, it checks 
the temperature to give, if it is true it will print a message for warm 
weather, if false it will print a message for chilly weather. If the first 
condition is false, it checks if it is raining and prints a message 
accordingly. If none of the conditions are met, it prints a message about 
unpredictable weather."""
if good_weather:
    if temperature > 20:
        print("It's warm and sunny! Perfect for a picnic.")
    else:
        print("It's a nice day, but a bit chilly. Maybe wear a light jacket.")
elif is_raining:
    print("It's raining. Don't forget your umbrella!")
else:
    print("The weather is unpredictable. Check the forecast before going out.")


# Example with multiple conditions
"""This example uses logical operators to combine multiple conditions. It 
checks if the weather is good and the temperature is above 15 degrees for 
outdoor activities. if the good_ weather is false it checks if it is raining 
or the temperature is below 5 degrees to suggest staying indoors. If none of 
these conditions are met, it suggests that the weather is moderate. 
IMPORTANT: AND operator returns true if both conditions are true, OR operator 
returns true if at least one condition is true."""
if good_weather and temperature > 15:
    print("Great weather for outdoor activities!")
elif is_raining or temperature < 5:
    print("Not the best weather for going out.")
else:
    print("Weather is moderate. You can decide based on your preference.")