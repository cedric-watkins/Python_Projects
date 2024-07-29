"""
This program interprets the Body Mass Index (BMI) value based on a user's weight and height.

BMI Categories:
- Under 18.5: Underweight
- 18.5 to 24.9: Normal weight
- 25 to 29.9: Slightly overweight
- 30 to 34.9: Obese
- 35 and above: Clinically obese

Methods and Tools:
1. input(): Captures user input from the console.
2. float(), int(): Converts input strings to numbers.
3. **: Performs exponentiation to square the height.
4. /: Divides weight by the squared height to calculate BMI.
5. if/elif: Executes code blocks based on BMI value.
6. print(): Outputs BMI and category to the console.
"""

# Request height in meters
height = float(input("How tall are you (in meters): "))

# Request weight in kilograms
weight = int(input("How much do you weigh (in kilograms): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print out BMI value based on specific conditions
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
