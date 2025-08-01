# Week 7 Regular Expressions Problem Set 7 Regluar, um, Expressions um.py with test_um.py
#
# In a file called um.py, implement a function called count that expects a line of text as input as a str and returns,
# as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself,
# not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1.
# Given text like yummy, though, the function should return 0.

# Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# import re
# import sys

# def main():
#     print(count(input("Text: ")))
#
# def count(s):
#
# if __name__ == "__main__":
#     main()
#
# How to Test um.py
# Here’s how to test um.py manually:
# Run your program with python um.py. Ensure your program prompts you for an input.
# Type um, followed by Enter. Your count function should return 1.
# Run your program with python um.py. Type um?, followed by Enter.
# Your count function should return 1.
# Run your program with python um.py. Type Um, thanks for the album., followed by Enter.
# Your count function should return 1.
# Run your program with python um.py. Type Um, thanks, um..., followed by Enter.
# Your count function should return 2.

import re

def main():
    print(count(input("Text: ")))


def count(s):
    # test \b\W*um\W regex in https://regex101.com/ with um... for a positive matching test and yummy for a negative matching test
#    um_list = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    um_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_list)


if __name__ == "__main__":
    main()
