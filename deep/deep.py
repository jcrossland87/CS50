# Week 1 Problem Set 1 Deep Thought deep.py

# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42
# or (case-insensitively) forty-two or forty two. Otherwise output No.

# Acceptance criteria for input giving output as expected is:
# 42 input Yes output
# Forty Two input Yes output
# forty-two input Yes output
# 50 input No output
# Need to be able to vary the case and add spaces either side of input.
# unit test with check50 cs50/problems/2022/python/deep
# submit with submit50 cs50/problems/2022/python/deep

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")
    





