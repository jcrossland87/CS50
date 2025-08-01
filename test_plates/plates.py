# Week 5 Problem Set 5 Re-requesting a vanity plate plates.py refactored for pytest test_plates.py using is_valid(s) function

# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid
# if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s
# input will be uppercase. Structure your program per the below, wherein is_valid returns True
# if s meets all requirements and False if it does not. Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# Hints Hints Recall that a str comes with quite a few methods, per
# docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is a “sequence” (of characters),
# which means it can be “sliced” into shorter strings with syntax like s[i:j].
# For instance, if s is "CS50", then s[0:2] would be "CS".

# Acceptance criteria for input giving output as expected is:
# Type CS50 and press Enter. Your program should output: Valid
# Type CS05 and press Enter. Your program should output: Invalid
# Type CS50P and press Enter. Your program should output: Invalid
# Type PI3.14 and press Enter. Your program should output: Invalid
# Type H and press Enter. Your program should output: Invalid
# Type OUTATIME and press Enter. Your program should output: Invalid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate;
    # AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # If we pass all the tests, return True
    return True


main()
