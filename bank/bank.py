# Week 1 Problem Set 1 Home Federal Savings Bank bank.py

# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Acceptance criteria for input giving output as expected is:
# Hello input $0 output
# Hello, Newman input $0 output
# How you doing? input $20 output
# What's happening? input $100 output

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
