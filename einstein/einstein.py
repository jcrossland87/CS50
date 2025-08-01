# einstein.py

# E = mc2 E is energy measured in Joules m is mass in kilograms c is speed of light 300000000 meters second
# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# speed of light c = 300000000 meters second - defined as global variable C using capitals as Python standard

C = 300000000

# Define main() function that inputs mass as an integer and prints the E = mc2 formula calculation as an integer

def main():
    mass = int(input("m: "))
    print("E:", calculate(mass))

# Define calculate() function that calculates E = mc2 using return with mass * (C ** 2) with global variable C

def calculate(mass):
    return mass * (C ** 2)


main()

