# Week 8 Object-Oriented Programming Problem Set 8 Seasons of Love seasons.py with test_seasons.py
#
# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD
# format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals,
# just like the song from Rent, without any and between words. Since a user might not know the time at which they were born,
# assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight.
# In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.
# Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
#
# Structure your program per the below, not only with a main function but also with one or more other functions as well:
#
# from datetime import date
#
# def main():
#
#
# if __name__ == "__main__":
#     main()
#
# You’re welcome to import other (built-in) libraries, or any that are specified in the below hints.
# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.
#
# Hints
# Note that the date class comes with quite a few methods and “supported operations,” per docs.python.org/3/library/datetime.html#date-objects.
# In particular, the class implements __sub__, per docs.python.org/3/library/operator.html#operator.__sub__, overloading - in such a way that
# subtracting one date object from another returns a timedelta object, which itself comes with several (read-only) “instance attributes,”
# per docs.python.org/3/library/datetime.html#timedelta-objects.
# Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
# pip install inflect
#
# How to Test seasons.py
# Here’s how to test seasons.py manually:
#
# Run your program with python seasons.py. Ensure your program prompts you for a birthdate.
# Type a date one year ago from today, in the specified format, then press Enter.
# Your program should sing print Five hundred twenty-five thousand, six hundred minutes.
# If this is a leap year, there should be one more day’s worth of minutes, so expect Five hundred twenty-seven thousand forty minutes instead!
# Run your program with python seasons.py. Type a date two years ago from today, in the specified format, then press Enter.
# Your program should print One million, fifty-one thousand, two hundred minutes (or One million, fifty-two thousand, six hundred forty minutes in a leap year).
# Run your program with python seasons.py. Type a date of your choice, but this time use an invalid format.
# Press Enter and your program should exit using sys.exit without raising an Exception.

import sys
import re
# test regex on https://regex101.com/ first before testing in pytest
import inflect

p = inflect.engine()

from datetime import date

def main():
    birth_date = input("Date of Birth: ")
    try:
        year,  month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + " minutes")

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
