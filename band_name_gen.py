"""
This program generates a band name based on the user's city and pet name.

Methods and Tools:
1. print(): Outputs messages to the console.
2. input(): Captures user input from the console.
3. string concatenation: Combines the city and pet names to form the band name.
"""

# Welcome the player to the band name generator
print("\nHello, welcome to the Band Name Generator")

# Ask the user what city they grew up in
city_name = input("\nWhat city did you grow up in?\n")

# Ask the user the name of their pet
pet_name = input("\nWhat is the name of your pet?\n")

# Generate the band name by combining the city they grew up in and their pet name
print("\nYour band name could be " + city_name + " " + pet_name + "\n")
