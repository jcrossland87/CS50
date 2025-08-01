# Week 2 Problem Set 2 camelCase camel.py

# In a file called camel.py, implement a program that
# prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

# Hints Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop.
# For instance, if s is a str, you could print each of its characters, one at a time, with code like:
# for c in s:
#    print(c, end="")

# Acceptance criteria for input giving output as expected is:
# Type name and press Enter. Your program should output: name
# Type firstName and press Enter. Your program should output: first_name
# Type preferredFirstName and press Enter. Your program should output: preferred_first_name

# Get user input
camelCase = input("camelCase: ")

# Print "snake_case: "
print("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:

    # Check if letter is upper case
    if letter.isupper():

        # Print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")

    # Otherwise print letter
    else:
        print(letter, end="")

# Print space at the end
print()



