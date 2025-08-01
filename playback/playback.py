# playback.py

# In a file called playback.py, implement a program in Python that
# prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

input_text = input("Enter text to replace single spaces with triple periods: ")

# Change single spaces to triple periods

output_text = input_text.replace(" ", "...")

# Print changed input as output with periods

print(output_text)
