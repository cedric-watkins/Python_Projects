"""
Calculate the love score of two individuals using their names, and returns a message based on the returned value.

Methods and Tools:
1. input(): Captures user input from the console.
2. lower(): Converts the input string to lowercase to ensure case insensitivity.
3. map(): Applies a function to all the items in an input list. 
4. sum(): Sums up all the items in an iterable.
5. str(): Converts a given value to a string.
6. int(): Converts a given value to an integer.
7. if/elif/else: Executes code blocks based on conditional statements.
8. f-string: Formats the output to include calculated values.
"""

# Get the names of both people
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

# Combine both names
combined_names = name1 + name2

# Calculate the score for the word "TRUE"
char_true = sum(map(combined_names.count, ['t', 'r', 'u', 'e']))

# Calculate the score for the word "LOVE"
char_love = sum(map(combined_names.count, ['l', 'o', 'v', 'e']))

# Combine the scores to make a 2-digit number
love_score = int(str(char_true) + str(char_love))

# Determine the message based on the love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
