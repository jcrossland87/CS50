# Week 6 File I/O Problem Set 6 Lines of Code lines.py

# in a file called lines.py, implement a program that expects exactly one command-line argument,
# the name (or path) of a Python file, and outputs the number of lines of code in that file,
# excluding comments and blank lines. If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py, or if the specified file does not exist,
# the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods,
# including lstrip and startswith.
# Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.

# How to Test
# Here’s how to test your code manually:

# Run your program with python lines.py. Your program should exit with sys.exit and provide an error message:
# Too few command-line arguments
# Create two python programs, hello.py and goodbye.py. Run python lines.py hello.py goodbye.py.
# Your program should exit with sys.exit and provide an error message:
# Too many command-line arguments
# Create a text file called invalid_extension.txt. Run your program with python lines.py invalid_extension.txt.
# Your program should exit with sys.exit and provide an error message:
# Not a Python file
# Run your program with python lines.py non_existent_file.py.
# Assuming non_existent_file.py doesn’t exist, your program should exit with sys.exit and provide an error message:
# File does not exist

import sys

def main():
    # Check the command line arguments
    check_command_line_arg()
    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    # If cannot open the file this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Loop through the lines of code to check if it starts with a comment # or whitespace
    count_lines = 0
    for line in lines:
        if check_comment_or_empty_line(line) == False:
            count_lines += 1
    print(count_lines)

# Function to check the command line arguments
def check_command_line_arg():
    # Check how many elements are in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if a Python file exists
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
