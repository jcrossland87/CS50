# Week 5 Problem Set 5 Home Federal Savings Bank bank.py refactored for unit test with pytest

# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Acceptance criteria for input giving output as expected is:
# Hello input $0 output
# Hello, Newman input $0 output
# How you doing? input $20 output
# What's happening? input $100 output

# In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below,
# wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h”
# (but not “hello”), or 100 otherwise, treating the str case-insensitively.
# You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.
# def main()
#     ...
# def value(greeting):
#     ...
# if __name__ == "__main__":
#   main()
# Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:
# pytest test_bank.py
# How to Test
# To test your tests, run pytest test_bank.py. Be sure you have a copy of a bank.py file in the same folder.
# Try to use correct and incorrect versions of bank.py to determine how well your tests spot errors:
# Ensure you have a correct version of bank.py. Run your tests by executing pytest test_bank.py.
# pytest should show that all of your tests have passed.
# Modify the correct version of bank.py, changing the values provided for each greeting.
# Your program might, for example, mistakenly provide $100 to a customer greeted by “Hello” and $0 to a customer greeted with “What’s up”!
# Now, run your tests by executing pytest test_bank.py. pytest should show that at least one of your tests has failed.

# Commented out the original bank.py below to run new bank.py using main() and value(greeting) functions needed for pytest test_bank.py
# greeting = input("Greeting: ").strip().lower()
# if greeting.startswith("hello"):
#     print("$0")
# elif greeting[0] == "h":
#     print("$20")
# else:
#     print("$100")
# Refactored the above original bank.py with the new bank.py using main() and value(greeting) functions needed for pytest test_bank.py
def main():
    # Get user input
    greeting = input("Greeting: ")
    # Store the result in the value (greeting) function
    value_to_print = value(greeting)
    print(f"${value_to_print}")

def value(greeting):
    # Convert greeting to lowercase without spaces
    greeting = greeting.lower().strip()
    # Check if the greeting contains 'hello' then return 0 dollars
    if 'hello' in greeting:
        return 0
    # Check if the greeting starts with 'h' then return 20 dollars
    elif 'h' == greeting[0]:
        return 20
    # Else return 100 dollars
    else:
        return 100

if __name__ == "__main__":
    main()
