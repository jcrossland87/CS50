# Week 7 Regular Expressions Problem Set 7 Working 9 to 5 working.py

# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below
# and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized
# (with no periods therein) and that there will be a space before each. Assume that these times are representative of
# actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
# (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# import re
# import sys
#
#
# def main():
#    print(convert(input("Hours: ")))
#
#
# def convert(s):
#    ...
# ...
#
#
#if __name__ == "__main__":
#    main()
#

# Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py,
# three or more functions that collectively test your implementation of convert thoroughly, each of whose names should
# begin with test_ so that you can execute your tests with:

#pytest test_working.py

# Hints
# Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
# Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
# Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for
# regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed
# with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
# Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,”
# per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group,
# per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

# How to Test working.py
# Here’s how to test working.py manually:

# Run your program with python working.py. Ensure your program prompts you for a time. Type 9 AM to 5 PM, followed by Enter.
# Your program should output 09:00 to 17:00.
# Run your program with python working.py. Type 9:00 AM to 5:00 PM, followed by Enter.
# Your program should again output 09:00 to 17:00.
# Run your program with python working.py. Ensure your program prompts you for a time. Type 10 AM to 8:50 PM, followed by Enter.
# Your program should output 10:00 to 20:50.
# Run your program with python working.py. Ensure your program prompts you for a time. Type 10:30 PM to 8 AM, followed by Enter.
# Your program should output 22:30 to 08:00.
# Run your program with python working.py. Ensure your program prompts you for a time.
# Try intentionally inducing a ValueError by typing 9:60 AM to 5:60 PM, followed by Enter.
# Your program should indeed raise a ValueError.
# Run your program with python working.py. Ensure your program prompts you for a time.
# Try intentionally inducing a ValueError by typing 9 AM - 5 PM, followed by Enter.
# Your program should indeed raise a ValueError.
# Run your program with python working.py. Ensure your program prompts you for a time.
# Try intentionally inducing a ValueError by typing 09:00 AM - 17:00 PM, followed by Enter.
# Your program should indeed raise a ValueError.

import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # test regex online with ^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$ at https://regex101.com/
    # test strings for regex101.com to enter below regular expression entered
    # 9:00 AM to 5.00 PM
    # 9 AM to 5 PM
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFormat:
        pieces = isCorrectFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + ' to ' + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ':00'
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time


if __name__ == "__main__":
    main()
