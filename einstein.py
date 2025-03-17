# einstein.py

# E = mc2 E is energy measured in Joules m is mass in kilograms c is speed of light 300000000 meters second
# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Prompt the user to input a mass as an integer in kilograms
mass = int(
    input(
        "Enter mass in kilograms as an integer to calculate energy of mass in Joules using Einstein's E = mc2 formula: "
    )
)

# Define constant as speed of light 30000000 meters second
# Use pow() function to make the constant squared to multiply

speed_of_light_constant = 300000000

base = speed_of_light_constant

exponent = 2

constant_squared = pow(base, exponent)

# Calculate the energy in Joules using Einstein's E = mc2 formula

energy = mass * constant_squared

# Print the energy in joules for a given mass converted to energy in Joules using Einstein's E = mc2 formula

print(
    "The energy in Joules for this mass converted using Einstein's E = mc2 formula is",
    energy,
)
