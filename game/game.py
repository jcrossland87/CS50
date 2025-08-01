# Week 4 Problem Set 4 Guessing Game game.py
# I’m thinking of a number between 1 and 100…

# What is it?
# It’s 50! But what if it were more random?

# In a file called game.py, implement a program that:

# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

# Hints Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
import random
# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass
# Set random number
random_number = random.randint(1, level)
# Get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
