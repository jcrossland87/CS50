# Week 6 File I/O Problem Set 6 Pizza Py pizza.py

# In a file called pizza.py, implement a program that expects exactly one command-line argument,
# the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
# a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
# or if the specified file does not exist, the program should instead exit via sys.exit.

# Hints
# Recall that the csv module comes with quite a few methods, per docs.python.org/3/library/csv.html,
# among which are reader, per docs.python.org/3/library/csv.html#csv.reader, and DictReader,
# per docs.python.org/3/library/csv.html#csv.DictReader.
# Note that open can raise a FileNotFoundError,
# per docs.python.org/3/library/exceptions.html#FileNotFoundError.
# Note that the tabulate package comes with just one function,
# per pypi.org/project/tabulate.
# You can install the package with:
# pip install tabulate

# How to Test
# Here’s how to test your code manually:

# Run your program with python pizza.py. Your program should exit using sys.exit and provide an error message:
# Too few command-line arguments
# Be sure to download regular.csv and sicilian.csv, placing them in the same folder as pizza.py.
# Run your program with python pizza.py regular.csv sicilian.csv. Your program should output:
# Too many command-line arguments
# Run your program with python pizza.py invalid_file.csv. Assuming invalid_file.csv doesn’t exist,
# your program should exit using sys.exit and provide an error message:
# File does not exist
# Create a file named sicilian.txt. Run your program with python pizza.py sicilian.txt.
# Your program should exit using sys.exit and provide an error message:
# Not a CSV file
# Run your program with python pizza.py regular.csv. Assuming you’ve downloaded regular.csv,
# your program should print a table like the below:
# +-----------------+---------+---------+
# | Regular Pizza   | Small   | Large   |
# +=================+=========+=========+
# | Cheese          | $13.50  | $18.95  |
# +-----------------+---------+---------+
# | 1 topping       | $14.75  | $20.95  |
# +-----------------+---------+---------+
# | 2 toppings      | $15.95  | $22.95  |
# +-----------------+---------+---------+
# | 3 toppings      | $16.95  | $24.95  |
# +-----------------+---------+---------+
# | Special         | $18.50  | $26.95  |
# +-----------------+---------+---------+

import sys
import csv
from tabulate import tabulate

def main():
    # Check the command line arguments
    check_command_line_arg()
    # Create variable to store the table data
    table = []
    # Try to open the CSV file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    # If cannot open the file this means that the CSV file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Print the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

# Function to check the command line arguments
def check_command_line_arg():
    # Check how many elements are in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
