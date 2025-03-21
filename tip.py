# tip.py

# In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost.
# Not to worry, though, we’ve written a tip calculator for you, below!

# Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
# dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
# remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
# percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
# remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
# Assume that the user will input values in the expected formats.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# Replace $ sign with nothing using replace() and convert as a float()


def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)


# Replace % sign with nothing using replace() and convert as a float()


def percent_to_float(p):
    p_without_percent_sign = p.replace("%", "")
    p_converted = float(p_without_percent_sign) / 100
    return p_converted


main()
