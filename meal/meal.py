# Week 1 Problem Set 1 Meal Time meal.py

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time,
# lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive. For instance, whether it’s
# 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main)
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

# Hints Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods,
# including split, which separates a str into a sequence of values, all of which can be assigned to variables at once.
# For instance, if time is a str like "7:30", then
# hours, minutes = time.split(":")
# will assign "7" to hours and "30" to minutes. Keep in mind that there are 60 minutes in 1 hour.

def main():
    # Get time from user
    answer = input("What time is it? ")
    # Call convert function
    time = convert(answer)
    # breakfast from 7:00 to 8:00
    if time >=7 and time <= 8:
        print("breakfast time")
    # lunch from 12:00 to 13:00
    if time >=12 and time <= 13:
        print("lunch time")
    # dinner from 18:00 to 19:00
    if time >=18 and time <= 19:
        print("dinner time")

def convert(time):
    # Get hours and minutes
    hours, minutes = time.split(":")
    # Convert time to float
    float_minutes = float(minutes) / 60
    # Return result to main()
    return float(hours) + float_minutes

if __name__ == "__main__":
    main()

