"""
This is a simple program to practice conditionals in Python.
The program calculates the down payment for a house based on the buyer's credit status.

Story:
price of a house is $1,000,000
if a buyer has good credit:
    they need to put down 20%
if a buyer has bad credit:
    they need to put down 30%
Print the down payment and other loan details.
"""

# Define house price
house_price = 1000000  # Price of the house

# Prompt the user to input their saving amount
buyers_credit = float(input("Enter your savings amount: "))

# Determine down payment percentage based on buyer's credit
if buyers_credit == 0:
    print("Loan Denied: You have no savings for the down payment.")
else:
    # Determine credit status
    if buyers_credit >= 250000:
        down_payment_percentage = 0.2
        status = "Good Credit"
    else:
        down_payment_percentage = 0.3
        status = "Bad Credit"

    # Calculate down payment and remaining loan amount
    down_payment = house_price * down_payment_percentage
    loan_amount = house_price - down_payment

    # Display loan details
    print("Loan Approved -- Summary")
    print(f"House Price: ${house_price:,.2f}")
    print(f"Buyer's Savings: ${buyers_credit:,.2f}")
    print(f"Buyer's Credit Status: {status}")
    print(f"Down Payment: ${down_payment:,.2f}")
    print(f"Loan Amount: ${loan_amount:,.2f}")