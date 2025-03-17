# faces.py

# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input
# with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any ( converted to 🙁
# (otherwise known as a slightly frowning face). All other text should be returned unchanged.

# Define a main() function that gets input and sends it for conversion output and prints the returned output


def main():
    # Get the user input
    print(
        "Enter a happy face :-) for conversion to 🙂 or enter a sad face :-( for conversion to 🙁"
    )
    str_input = input()

    # Call the convert function and defines output from input when returned converted
    str_output = convert(str_input)

    # Print the converted output from the returned value in convert(str_input) with converted2 returned
    print(str_output)


# Define a convert(str_input) function that converts input and returns output


def convert(str_input):
    # Replace :-) with 🙂
    converted1 = str_input.replace(":-)", "🙂")
    # Replace :-( with 🙁
    converted2 = converted1.replace(":-(", "🙁")
    # Return converted string with 🙂 from :-) or 🙁 from :-(
    # Returning converted2 will show 🙁 if :-( entered or will show converted1 if :-) entered as no :-( to replace
    return converted2


# Call defined main() function

main()
