"""
This program prompts the user to enter a number and determines whether the number is even or odd.
It then prints a message indicating the result.


Methods and Programming Tools Used:
1. Input Function: The `input()` function is used to capture user input from the console.
2. Type Conversion: The `int()` function is used to convert the user input from string to integer.
3. Modulo Operator: The `%` operator determines the remainder to check if even or odd.
4. Conditional Statements: The `if` and `else` statements executes code blocks based on conditions.
5. Print Function: The `print()` function is used to output messages to the console.
"""

# Prompt the user to enter a number and convert the input to an integer
number = int(input("Enter a number: "))

# Check if the number is even by using the modulo operator
# An even number will have a remainder of 0 when divided by 2
if number % 2 == 0:
    # If the condition is true, print that the number is even
    print("This is an even number.")
else:
    # If the condition is false, print that the number is odd
    print("This is an odd number.")
