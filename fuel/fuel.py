# Week 3 Problem Set 3 Fuel Gauge fuel.py

# Fuel gauges indicate, often with fractions,
# just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
# 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# Hints Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
# Note that you can handle two exceptions separately with code like:
# try:
#    ...
# except ValueError:
#    ...
# except ZeroDivisionError:
#    ...
# Or you can handle two exceptions together with code like:
# try:
#    ...
# except (ValueError, ZeroDivisionError):
#    ...

# Acceptance criteria for input giving output as expected is:
# Type 3/4 and press Enter. Your program should output: 75%
# Run your program with python fuel.py. Type 1/4 and press Enter. Your program should output: 25%
# Run your program with python fuel.py. Type 4/4 and press Enter. Your program should output: F
# Run your program with python fuel.py. Type 0/4 and press Enter. Your program should output: E
# Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.
# Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.
# Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.
# Type 5/4 and press Enter. Your program should prompt the user again.
# used import math for math.ceil to round up so 2/3 = 67% for check50
import math
# While forever
while True:
    # Get user input
    fuel = input("Fraction: ")
    try:
        # Try to split the fuel
        numerator, denominator = fuel.split("/")
        # Convert into integers
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        # Calculate the percentage
        f = (new_numerator / new_denominator)
        # Check if its less than 1 and stop the loop
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# Multiply percentage by 100
p = math.ceil(f * 100)
# Check if percentage is less than 1, print E
if p <= 1:
    print("E")
# Check if percentage is greater than 99, print F
elif p >= 99:
    print("F")
# Otherwise, print the %
else:
    print(f"{p}%")
