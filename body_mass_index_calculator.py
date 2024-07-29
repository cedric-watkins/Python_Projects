"""
Program used to calculate Body Mass Index (BMI).
This program takes the user's height in meters and weight in kilograms as input,
and calculates the BMI using the formula: weight / (height ** 2).
It then prints the calculated BMI.

Methods and Tools:
1. input(): Captures user input from the console.
2. float(): Converts the input string to a floating-point number.
3. **: Exponentiation operator to square the height.
4. /: Division operator to calculate BMI.
5. str(): Converts the BMI result to a string.
6. int(): Converts the BMI result to an integer for output.
7. print(): Outputs the BMI to the console.
"""

# 1st input: enter height in meters e.g: 1.65
height = float(input("Enter height in meters (e.g., 1.65): "))

# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Enter weight in kilograms (e.g., 72): "))

# Calculate BMI using the formula: weight / (height ** 2)
bmi = weight / (height ** 2)

# Print the calculated BMI as an integer
print("Your BMI is: " + str(int(bmi)))
