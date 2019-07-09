"""
    You need to write a function, that returns the first non-repeated character in the given string.

    For example for string "test" function should return 'e'.
    For string "teeter" function should return 'r'.

    If a string contains all unique characters, then return just the first character of the string.
    Example: for input "trend" function should return 't'

    You can assume, that the input string has always non-zero length.

    Sample Tests:

        Test.it("Basic tests")
        Test.assert_equals(first_non_repeated("test"),'e')
        Test.assert_equals(first_non_repeated("teeter"),'r')
        Test.assert_equals(first_non_repeated("1122321235121222"),'5')

"""


def first_non_repeated(s):
    for x in s:
        if s.count(x) == 1:
            return x
