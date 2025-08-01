# Week 7 Regular Expressions Problem Set 7 Response Validation response.py
#
# In a file called response.py, using either validator-collection or validators from PyPI,
# implement a program that prompts the user for an email address via input and then prints Valid or Invalid,
# respectively, if the input is a syntatically valid email address. You may not use re.
# And do not validate whether the email address’s domain name actually exists.
#
# Hints
# Note that you can install validator-collection with:
# pip install validator-collection
# Click Homepage to find your way to the library’s documentation.
# https://pypi.org/project/validator-collection/
#
# See sample code listed below for email validation with validator-collection package installed with pip install validator-collection
# from https://pypi.org/project/validator-collection/
#
# from validator_collection import validators, checkers, errors
#
# email_address = validators.email('test@domain.dev')
# The value of email_address will now be "test@domain.dev"
# email_address = validators.email('this-is-an-invalid-email')
# Will raise a ValueError
# try:
#     email_address = validators.email(None)
#     # Will raise an EmptyValueError
# except errors.EmptyValueError:
#     # Handling logic goes here
# except errors.InvalidEmailError:
#     # More handlign logic goes here
#
# email_address = validators.email(None, allow_empty = True)
# The value of email_address will now be None
#
# email_address = validators.email('', allow_empty = True)
# The value of email_address will now be None
#
# is_email_address = checkers.is_email('test@domain.dev')
# The value of is_email_address will now be True
#
# is_email_address = checkers.is_email('this-is-an-invalid-email')
# The value of is_email_address will now be False
#
# is_email_address = checkers.is_email(None)
# The value of is_email_address will now be False
#
# Here’s how to test your code manually:
# Run your program with python response.py. Ensure your program prompts you for an email, then type malan@harvard.edu, followed by Enter.
# Your program should output Valid.
# Run your program with python response.py. Type your own email, followed by Enter.
# Your program should output Valid.
# Run your program with python response.py. Type malan@@@harvard.edu, followed by Enter.
# Your program should output Invalid.
# Run your program with python response.py. Mistype your own email, including an extra . before .com, for example.
# Press enter and your program should output Invalid.
#


from validator_collection import validators

def main():
    email_address = input("What's your email address? ")
    try:
        emailIsValid = validators.email(email_address)
        print("Valid")
    except:
        print("Invalid")


if __name__ == "__main__":
    main()
