# Week 2 Problem Set 2 Coke Machine coke.py

# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
# and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Acceptance criteria for input giving output as expected is:

# At your Insert Coin: prompt, type 25 and press Enter.
# Your program should output: Amount Due: 25
# and continue prompting the user for coins.

# At your Insert Coin: prompt, type 10 and press Enter.
# Your program should output: Amount Due: 40
# and continue prompting the user for coins.

# At your Insert Coin: prompt, type 5 and press Enter.
# Your program should output: Amount Due: 45
# and continue prompting the user for coins.

# At your Insert Coin: prompt, type 30 and press Enter.
# Your program should output: Amount Due: 50
# and continue prompting the user for coins.

# At your Insert Coin: prompt, type 25 and press Enter, type 25 and press Enter.
# Your program should output: Change Owed: 0

# At your Insert Coin: prompt, type 25 and press Enter, type 10 and press Enter, type 25 and press Enter.
# Your program should output: Change Owed: 10

# Hint: Be careful to print the prompts and responses exactly as shown above.
# If your program prints any extra text, it may fail check50.

# Variable to keep track of amount due
amount_due = 50

# Loop until amount_due > 0
while amount_due > 0:
    # Print amount due
    print("Amount Due:", amount_due)
    # Tell user to insert a coin
    coin = int(input("Insert Coin:"))
    # Test if coin is 25, 10, or 5 cents
    if coin in [25, 10, 5]:
        # Subtract coin from amount_due
        amount_due -= coin

# Calculate change_owed
change_owed = abs(amount_due)
# Print result
print("Change Owed:", change_owed)
