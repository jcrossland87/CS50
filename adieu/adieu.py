# Week 4 Problem Set 4 Adieu, Adieu adieu.py

# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

# Adieu, adieu, to yieu and yieu and yieu

# Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

# Adieu, adieu, to yieu, yieu, and yieu

# To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
# Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and, and n names with n-1 commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

# Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
# pip install inflect

# run pip install inflect on command line before import inflect run with python adieu.py - must install before import

import inflect

p = inflect.engine()

# Create list to keep track of names

names = []

# Loop forever

while True:
    try:
    # Get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break
# Print using inflect package
output = p.join(names)
print("Adieu, adieu, to " + output)
