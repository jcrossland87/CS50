# Week 7 Regular Expressions Problem Set 7 Regluar, um, Expressions test_um.py with um.py
#
# Either before or after you implement count in um.py, additionally implement, in a file called test_um.py,
# three or more functions that collectively test your implementation of count thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:
#
# pytest test_um.py
#
# How to Test test_um.py
# To test your tests, run pytest test_um.py. Try to use correct and incorrect versions of um.py to determine
# how well your tests spot errors:
# Ensure you have a correct version of um.py. Run your tests by executing pytest test_um.py.
# pytest should show that all of your tests have passed.
# Modify the count function in the correct version of um.py. count might, for example,
# mistakently also count any “um” that is part of a word. Run your tests by executing pytest test_um.py.
# pytest should show that at least one of your tests has failed.
# Again modify the count function in the correct version of um.py. count might, for example,
# mistakenly only match an “um” that is surrounded on either side by a space.
# Run your tests by executing pytest test_um.py. pytest should show that at least one of your tests has failed.
#
from um import count

def main():
    test_upper_lower_case()
    test_word_with_um()
    test_surrounded_by_space()

def test_upper_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_word_with_um():
    assert count('yummy') == 0
    assert count('mummy') == 0

def test_surrounded_by_space():
    assert count('Hello um world') == 1
    assert count('um?') == 1

if __name__ == "__main__":
    main()
