# Week 1 Problem Set 1 Math Interpreter interpreter.py

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer y is +, -, *, or / z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
# Hint to use str with method split that separates a str into a sequence of values which can be asssigned to variables:
# x, y, z = expression.split(" ") will assign 1 + 1 as 1 to x and + to y and 1 to z

# Acceptance criteria for input giving output as expected is:
# 1 + 1 input 2.0 output 2 - 3 input -1.0 output 2 * 2 input 4.0 output 50 / 5 input 10.0 output

# Get user input

expression = input("Expression: ")

# Convert input into variables x y z 

x, y, z = expression.split(" ")

# Convert x y z variables to float

float_x = float(x)

float_z = float(z)

# Calculate and print the result

if y == "+":
    result = float_x + float_z
if y == "-":
    result = float_x - float_z
if y == "*":
    result = float_x * float_z
if y == "/":
    result = float_x / float_z
print(result)


