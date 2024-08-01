"""
This program will allow the user to check if any given year is a leap year or not.

Methods and Tools:
1. input(): Captures user input from the console.
2. int(): Converts input string to an integer.
3. Nested if/else: Executes code blocks based on leap year conditions.
4. print(): Outputs whether the year is a leap year or not.
"""

# Get the user to input the year they would like to check
year = int(input("Which year do you want to check? "))

# Determine if the year is a leap year
if year % 4 == 0:  # Check if the year is divisible by 4
    if year % 100 == 0:  # Nested if: Check if the year is divisible by 100
        if year % 400 == 0:  # Nested if within the second if: Check if the year is divisible by 400
            # If the year is divisible by 400, it is a leap year
            print("Leap year")
        else:
            # If the year is divisible by 100 but not by 400, it is not a leap year
            print("Not leap year")
    else:
        # If the year is divisible by 4 but not by 100, it is a leap year
        print("Leap year")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("Not leap year")
