"""
This program simulates a Rock-Paper-Scissors game where the user plays against the computer.

Methods and Tools:
1. random.choice(): Randomly selects an item from a list.
2. print(): Outputs messages to the console.
3. f-string: Formats strings to include variables, enhancing readability and clarity.
4. if/elif/else: Determines the game outcome based on user and computer choices.
5. "or" operator: Combines multiple conditions in a single statement.
"""

import random

# List of possible game choices
game_choices = ["rock", "paper", "scissors"]

# User chooses to either Rock, Paper, or Scissors
user_input = input(
    'What do you choose? "Rock", "Paper", or "Scissors": ').lower()

# Display user's choice with ASCII art
print(f"\nYou chose {user_input}:")

if user_input == "rock":
    print(""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_input == "paper":
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:  # user_input == "scissors"
    print(""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Computer randomly chooses an item
computer_choice = random.choice(game_choices)

# Display computer's choice with ASCII art
print(f"\nComputer chose {computer_choice}:")

if computer_choice == "rock":
    print(""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == "paper":
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:  # computer_choice == "scissors"
    print(""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Determine the game outcome
if user_input == computer_choice:
    # Outcome if both choices are the same
    print("It's a Tie!")
elif (user_input == "rock" and computer_choice == "scissors") or \
     (user_input == "paper" and computer_choice == "rock") or \
     (user_input == "scissors" and computer_choice == "paper"):
    # Outcome if the user wins
    print("You Win!!!")
else:
    # Outcome if the computer wins
    print("You Lose.")
