"""
This program will automate the pizza order process based on the user's order and work out their final bill.

Methods and Tools:
1. print(): Outputs messages to the console.
2. input(): Captures user input from the console.
3. Nested if/else: Executes code blocks based on user choices.
4. +=: Increments the bill by adding the cost of selected items.
5. exit(): Terminates the program if an invalid input is given.
"""

# Welcome them to Python Pizza
print("Thank you for choosing Python Pizza!")

# Get input for pizza size
size = input("What size pizza would you like? S, M, or L: ").upper()

# Ask if they'd like pepperoni on their pizza
pepperoni = input("Do you want pepperoni? Y or N: ").upper()

# Would they like extra cheese
cheese = input("Would you like to add extra cheese? Y or N: ").upper()

# Set bill count to $0
bill = 0

# Determine the cost based on the size of the pizza and add-ons
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
else:
    print("Invalid size input")
    exit()

# Print the final bill
print(
    f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
