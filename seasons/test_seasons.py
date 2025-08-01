# Week 8 Object-Oriented Programming Problem Set 8 Seasons of Love test_seasons.py with seasons.py
#
# Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py,
# one or more functions that test your implementation of any functions besides main in seasons.py thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:
#
# pytest test_seasons.py
#
# How to Test test_seasons.py
# To test your tests, run pytest test_seasons.py.
# Try to use correct and incorrect versions of seasons.py to determine how well your tests spot errors:

# Ensure you have a correct version of seasons.py. Run your tests by executing pytest test_seasons.py. pytest should show that all of your tests have passed.
# Modify one of the functions you’ve implemented in seasons.py and imported into test_seasons.py.
# One of your functions might, for example, fail to raise a ValueError when it should. Run your tests by executing pytest test_seasons.py.
# pytest should show that at least one of your tests has failed.
# Continue to modify the behavior of seasons.py, creating (predictably) incorrect versions of your implementation.
# Run your tests by executing pytest test_seasons.py. Do the tests you expect to fail, fail?
#
from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday('1968-03-10') == ("1968", "03", "10")
    assert check_birthday('1968-3-10') == None
    assert check_birthday("March 10, 1968") == None


if __name__ == "__main__":
    main()

