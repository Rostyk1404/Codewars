"""
    Kata source :

        https://www.codewars.com/kata/regex-validate-pin-code/train/python

    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly
    4 digits or exactly 6 digits.

    If the function is passed a valid PIN string, return true, else return false.

    Sample Tests:

        Test.describe("validate_pin")

        Test.it("should return False for pins with length other than 4 or 6")
        Test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
        Test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
        Test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
        Test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
        Test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
        Test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
        Test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
        Test.assert_equals(validate_pin("-1.234"),False, "Wrong output for '-1.234'")
        Test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")

        Test.it("should return False for pins which contain characters other than digits")
        Test.assert_equals(validate_pin("a234"),False, "Wrong output for 'a234'")
        Test.assert_equals(validate_pin(".234"),False, "Wrong output for '.234'")
        Test.assert_equals(validate_pin("-123"),False, "Wrong output for '-123'")
        Test.assert_equals(validate_pin("-1.234"),False, "Wrong output for '-1.234'")

        Test.it("should return True for valid pins")
        Test.assert_equals(validate_pin("1234"),True, "Wrong output for '1234'")
        Test.assert_equals(validate_pin("0000"),True, "Wrong output for '0000'")
        Test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
        Test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        Test.assert_equals(validate_pin("098765"),True, "Wrong output for '098765'")
        Test.assert_equals(validate_pin("000000"),True, "Wrong output for '000000'")
        Test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        Test.assert_equals(validate_pin("090909"),True, "Wrong output for '090909'")

"""

import re


def validate_pin(pin):
    return bool(re.fullmatch("\d{4}|\d{6}", pin))


def validate_pin(pin):
    return True if len(pin) in (4, 6) and pin.isdigit() else False
