# Week 3 Problem Set 3 Outdated outdated.py

# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
# otherwise known as middle-endian order, which is arguably bad design.
# Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
# Dates in that format are also ambiguous.
# Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates
# should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting
# years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# [
#    "January",
#    "February",
#    "March",
#    "April",
#    "May",
#    "June",
#    "July",
#    "August",
#    "September",
#    "October",
#    "November",
#    "December"
# ]

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

# Hints Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
# Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

# Acceptance criteria for input giving output as expected is:
# Run your program with python outdated.py. Type 9/8/1636 and press Enter. Your program should output: 1636-09-08
# Run your program with python outdated.py. Type September 8, 1636 and press Enter. Your program should output: 1636-09-08
# Run your program with python outdated.py. Type 23/6/1912 and press Enter. Your program should reprompt the user.
# Run your program with python outdated.py. Type December 80, 1980 and press Enter. Your program should reprompt the user.

# Create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Loop forever
while True:
    # Get user input
    date = input("Date: ")
    try:
        # Split the date by /
        month, day, year = date.split("/")
        # Check if month is in between 1 through 12 and day between 1 through 31
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            # Split the date by space
            old_month, old_day, year = date.split(" ")
            # Find the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            # Remove comma from day variable
            day = old_day.replace(",","")
            # Check if month is in between 1 through 12 and day between 1 through 31
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            # Go to the next line
            print()
            pass

# If month is less than 10 then add a 0 before month
# If day is less than 10 then add a 0 before day
# Print the result with month and day with leading zero
print(f"{year}-{int(month):02}-{int(day):02}")







