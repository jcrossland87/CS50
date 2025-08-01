# Week 5 Problem Set 5 Re-requesting a vanity plate test_plates.py for pytest test_plates.py importing is_valid() function from plates.py
# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still
# expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value
# of __name__ is "__main__":
# def main():
#    ...
# def is_valid(s):
#    ...
# if __name__ == "__main__":
#    main()
# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:
# pytest test_plates.py
# Hints
# Be sure to include
# import plates
# or
# from plates import is_valid
# atop test_plates.py so that you can call is_valid in your tests.
# Take care to return, not print, a bool in is_valid. Only main should call print.
# How to Test
# To test your tests, run pytest test_plates.py. Be sure you have a copy of a plates.py file in the same folder.
# Try to use correct and incorrect versions of plates.py to determine how well your tests spot errors:
# Ensure you have a correct version of plates.py. Run your tests by executing pytest test_plates.py. pytest should show
# that all of your tests have passed.
# Modify the correct version of plates.py, perhaps eliminating some of its constraints.
# Your program might, for example, mistakenly print “Valid” for a license plate of any length!
# Run your tests by executing pytest test_plates.py. pytest should show that at least one of your tests has failed.

from plates import is_valid

def main():
    # Call test functions
    test_min_and_max_characters()
    test_start_with_two_letters()
    test_numbers_middle()
    test_number_zero()
    test_punctuation()

# Plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_min_and_max_characters():
    assert is_valid('A') == False
    assert is_valid('AB') == True
    assert is_valid('ABC') == True
    assert is_valid('ABCD') == True
    assert is_valid('ABCDE') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('ABCDEFG') == False

# Plates must start with at least two letters
def test_start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

# Numbers cannot be used in the middle of a plate; they must come at the end
def test_numbers_middle():
    assert is_valid('AA22') == True
    assert is_valid('A22A') == False

# The first number used cannot be a zero
def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

# No periods, commas, spaces or punctuation marks such as question marks or exclamation mark are allowed
def test_punctuation():
    assert is_valid('P13.14') == False
    assert is_valid('P13!14') == False
    assert is_valid('P13?14') == False
    assert is_valid('P13,14') == False
    assert is_valid('P13 14') == False

if __name__ == "__main__":
    main()
