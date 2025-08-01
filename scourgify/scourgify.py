# Week 6 File I/O Problem Set 6 Scourgify scourgify.py with before.csv imported to scourgify CS50 folder


# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.


# Hints
# Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are DictReader,
# per docs.python.org/3/library/csv.html#csv.DictReader and DictWriter, per docs.python.org/3/library/csv.html#csv.DictWriter.
# Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments,
# per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader.


# How to Test
# Here’s how to test your code manually:

# Run your program with python scourgify.py.
# Your program should exit using sys.exit and provide an error message:
# Too few command-line arguments
# Create empty files 1.csv, 2.csv, and 3.csv.
# Run your program with python scourgify.py 1.csv 2.csv 3.csv.
# Your program should output:
# Too many command-line arguments
# Run your program with python scourgify.py invalid_file.csv output.csv.
# Assuming invalid_file.csv doesn’t exist, your program should exit using sys.exit and provide an error message:
# Could not read invalid_file.csv
# Run your program with python scourgify.py before.csv after.csv.
# Assuming before.csv exists, your program should create a new file, after.csv,
# whose columns should be, in order, first, last, and house.

import sys
import csv

def main():
    # Check command line arguments
    check_command_line_arg()
    output = []
    # Try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({'first': split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
    # If cannot open the file then it does not exist
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    # Write new CSV file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def check_command_line_arg():
    # Check how many elements are in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()


