# Week 5 Unit Testing Problem Set 5 Just setting up my twttr twttr.py (for use with test_twttr.py and pytest so this has been refactored)
# See the description in Week 5 Unit Testing Testing my twttr test_twttr.py for the main() and shorten() functions that test_twttr.py calls

# When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
# implement a program that prompts the user for a str of text and then outputs that same text
# but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Hints Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop.
# For instance, if s is a str, you could print each of its characters, one at a time, with code like:
# for c in s:
#   print(c, end="")

# Acceptance criteria for input giving output as expected is:
# Type Twitter and press Enter. Your program should output: Twttr
# Type What's your name? and press Enter. Your program should output: Wht's yr nm?
# Type CS50 and press Enter. Your program should output: CS50

# Refactored for Week 5 Testing my Twttr to use main() and shorten() functions required for test_twttr.py and pytest

def main():
    # Get user input
    message = input("Input: ")
    # Remove all vowels
    message_without_vowels = shorten(message)
    # Print "Output: "
    print("Output: " + message_without_vowels)

def shorten(word):
    word_without_vowels = ""
    # Loop through every letter
    for letter in word:
        # Check for vowels entered in upper case or lower case
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            # Add the letter
            word_without_vowels += letter
    # Return the new word
    return word_without_vowels

if __name__ == "__main__":
    main()
