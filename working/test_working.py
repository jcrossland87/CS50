# Week 7 Regular Expressions Problem Set 7 Working 9 to 5 working.py

# How to Test test_working.py
# To test your tests, run pytest test_working.py. Try to use correct and incorrect versions of working.py
# to determine how well your tests spot errors:

# Ensure you have a correct version of working.py. Run your tests by executing pytest test_working.py.
# pytest should show that all of your tests have passed.
# Modify the correct version of working.py, particularly its function convert.
# Your program might, for example, fail to raise a ValueError when it should.
# Run your tests by executing pytest test_working.py. pytest should show that at least one of your tests has failed.
# Similarly, modify the correct version of working.py, changing the return values of convert.
# Your program might, for example, mistakenly omit minutes. Run your tests by executing pytest test_working.py.
# pytest should show that at least one of your tests has failed.

from working import convert
import pytest

def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

# negative test for wrong format
def test_wrong_format():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')

# positive test for correct time
def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

# negative test for wrong hour
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert('13 AM to 17 PM')

# negative test for wrong minute
def test_wrong_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM to 9:60 PM')

if __name__ == "__main__":
    main()
