# Week 5 Problem Set 5 Back to the bank test_bank.py refactored bank.py for unit test with pytest test_bank.py
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
#
# see refactored bank.py in test_bank folder for the value(greeting) function that is imported from bank.py into test_bank.py

from bank import value

def main():
    # Call test functions
    test_return_zero()

# Test returns 0 dollars
def test_return_zero():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('HeLlO') == 0

# Test returns 20 dollars
def test_return_twenty():
    assert value('hi') == 20
    assert value('Hi') == 20

# Test returns 100 dollars
def test_return_hundred():
    assert value('Gday') == 100
    assert value('gday') == 100

if __name__ == "__main__":
    main()
