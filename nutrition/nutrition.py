# Week 2 Problem Set 2 Nutrition Facts nutrition.py

# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit
# (case-insensitively) and then outputs the number of calories in one portion of that fruit,
# per the FDA’s poster for fruits, which is also available as text.
# Capitalization aside, assume that users will input fruits exactly as written in the poster
# (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

# Hint Rather than use a conditional with 20 Boolean expressions, one for each fruit,
# better to use a dict to associate a fruit with its calories!

# Acceptance criteria for input giving output as expected is:
# Type Apple and press Enter. Your program should output: Calories: 130
# Type Avocado and press Enter. Your program should output: Calories: 50
# Type Sweet Cherries and press Enter. Your program should output: Calories: 100
# Type Tomato and press Enter. Your program should output nothing.

# Create dictionary with all fruits and all calories
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# Get user input
fruit_asked = input("Item: ")

# Loop through fruit and calories dictionary
for key in fruits:

    # Find the fruit
    if key == fruit_asked.lower():

        # Print calories for fruit found
        print("Calories: ", fruits[key])


