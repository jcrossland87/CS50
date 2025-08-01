# Week 5 Unit Tests Problem Set 5 Refueling fuel.py refactored for pytest test_fuel.py to run main() and convert(fraction) functions

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

# In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
# co#nvert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a
# percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y,
# then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int
# def main():
#    ...
# def convert(fraction):
#    ...
# def gauge(percentage):
#    ...
# if __name__ == "__main__":
#    main()
# Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations
# of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
# pytest test_fuel.py
# Hints
# Be sure to include
# import fuel
# or
# from fuel import convert, gauge
# atop test_fuel.py so that you can call convert and gauge in your tests.
# Take care to return, not print, an int in convert and a str in gauge. Only main should call print.
# Note that you can raise an exception like ValueError with code like:
# raise ValueError
# Note that you can check with pytest whether a function has raised an exception, per
# docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.
# How to Test
# To test your tests, run pytest test_fuel.py. Be sure you have a copy of a fuel.py file in the same folder.
# Try to use correct and incorrect versions of fuel.py to determine how well your tests spot errors:
# Ensure you have a correct version of fuel.py. Run your tests by executing pytest test_fuel.py.
# pytest should show that all of your tests have passed.
# Modify the correct version of fuel.py, changing the return values of convert.
# Your program might, for example, mistakenly return a str instead of an int.
# Run your tests by executing pytest test_fuel.py. pytest should show that at least one of your tests has failed.
# Similarly, modify the correct version of fuel.py, changing the return values of gauge.
# Your program might, for example, mistakenly omit a % in the resulting str.
# Run your tests by executing pytest test_fuel.py. pytest should show that at least one of your tests has failed.

def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    # While forever
    while True:
        try:
            # Try to split the fuel
            numerator, denominator = fraction.split("/")
            # Convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            # Calculate the percentage
            f = (new_numerator / new_denominator)
            # Check if its less than 1 and stop the loop
            if f <= 1:
                # Multiply percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    # Check if percentage is less than 1, return E
    if percentage <= 1:
        return("E")
    # Check if percentage is greater than 99, return F
    elif percentage >= 99:
        return("F")
    # Otherwise, print the %
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
