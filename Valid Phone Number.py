"""
    Kata source :

            https://www.codewars.com/kata/valid-phone-number/train/python/5d27ba53f9092c001f7fff3c

    Write a function that accepts a string, and returns true if it is in the form of a phone number.
    Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

    Only worry about the following format:

        (123) 456-7890 (don't forget the space after the close parentheses)

    Examples:

        validPhoneNumber("(123) 456-7890")  =>  returns true
        validPhoneNumber("(1111)555 2345")  => returns false
        validPhoneNumber("(098) 123 4567")  => returns false

    Sample Tests:

        Test.assert_equals(validPhoneNumber("(123) 456-7890"), True)

"""
import re


def validPhoneNumber(phoneNumber):
    return True if len(phoneNumber) == 14 and phoneNumber.startswith("(") and phoneNumber[4].startswith(")") \
                   and phoneNumber[9] == "-" else False


def validPhoneNumberUsingRegularExpression(phoneNumber):
    return bool(re.fullmatch("\(\d{3}\)\s\d{3}-\d{4}", phoneNumber))
