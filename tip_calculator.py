""" 
This Program will allow a user calculate their tip based on the percentage they
would like to give, add it to the total price and split the bill amongst the group
"""

# Issue a greeting
print("\n*** Welcome to the tip calculator! ***")

# Get bill total
bill = float(input("What is your total bill? $"))

# Ask how much would they like to tip
tip = float(input("How much would you like to tip? "))

# Calculate new total for the bill
total_bill = round(bill * ((tip / 100) + 1), 2)

# Ask how is the bill being split and divide for total per person
people = int(input("How many people are splitting the bill? "))

per_person = round((total_bill / people), 2)

# Print out total per person
print(f"Each person should pay: ${per_person}\n")
