# Week 7 Regular Expressions Problem Set 7 test_numb3rs.py with numb3rs.py
#
# How to Test test_numb3rs.py
# To test your tests, run pytest test_numb3rs.py. Try to use correct and incorrect versions of numb3rs.py to determine how well your tests spot errors:
# Ensure you have a correct version of numb3rs.py. Run your tests by executing pytest test_numb3rs.py. pytest should show that all of your tests have passed.
# Modify the validate function in the correct version of numb3rs.py. validate might, for example, only check whether the first byte of the IPv4 address is valid.
# Run your tests by executing pytest test_numb3rs.py. pytest should show that at least one of your tests has failed.
# Again modify the correct version of numb3rs.py. validate might, for example, mistakenly return True when the user inputs an incorrect IPv4 format.
# Run your tests by executing pytest test_numb3rs.py. pytest should show that at least one of your tests has failed.
#
from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False

def test_range():
    assert validate('255.255.255.255') == True
    assert validate('512.1.1.1') == False
    assert validate('1.512.1.1') == False
    assert validate('1.1.512.1') == False
    assert validate('1.1.1.512') == False

if __name__ == "__main__":
    main()
