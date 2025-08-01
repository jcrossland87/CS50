# Week 4 Problem Set 4 Frank, Ian and Glen's Letters figlet.py

# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
#
#  _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/
# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

# Hints ou can install pyfiglet with:
# pip install pyfiglet
# The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
# from pyfiglet import Figlet

# figlet = Figlet()
# You can then get a list of available fonts with code like this:

# figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:

# figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:

# print(figlet.renderText(s))
# Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

# Acceptance criteria for input giving output as expected is:
# Run your program with python figlet.py test. Your program should exit via sys.exit and print an error message: Invalid usage
# Run your program with python figlet.py -a slant. Your program should exit via sys.exit and print an error message: Invalid usage
# Run your program with python figlet.py -f invalid_font. Your program should exit via sys.exit and print an error message: Invalid usage
# Run your program with python figlet.py -f slant. Type CS50. Your program should print the following:
#    ___________ __________
#   / ____/ ___// ____/ __ \
#  / /    \__ \/___ \/ / / /
# / /___ ___/ /___/ / /_/ /
# \____//____/_____/\____/
# Run your program with python figlet.py -f rectangles. Type Hello, world. Your program should print the following:
#  _____     _ _                        _   _
# |  |  |___| | |___      _ _ _ ___ ___| |_| |
# |     | -_| | | . |_   | | | | . |  _| | . |
# |__|__|___|_|_|___| |  |_____|___|_| |_|___|
#                   |_|
# Run your program with python figlet.py -f alphabet. Type Moo. Your program should print the following:
# M   M
# MM MM
# M M M ooo ooo
# M   M o o o o
# M   M ooo ooo

import sys

from pyfiglet import Figlet

import random

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit(1)

figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

print("Output:")
print(figlet.renderText(msg))
