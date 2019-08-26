"""
    Kata Source :

        https://www.codewars.com/kata/alternate-capitalization/train/python

    Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

    For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

    The input will be a lowercase string with no spaces.

    Good luck!

    If you like this Kata, please try:

        Indexed capitalization

        Even-odd disparity

    Sample Tests :

        Test.it("Basic tests")
        Test.assert_equals(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
        Test.assert_equals(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
        Test.assert_equals(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
        Test.assert_equals(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
"""


def capitalize(s):
    answer = "".join("".join(x.capitalize() if i % 2 == 0 else x for i, x in enumerate(letter)) for letter in s.split())
    # in this task we will capitalize all letter where index % 2 == 0. But before we will split our string because we
    # have to  enumerate it. For that we will build-in-methods: split and enumerate.
    return [answer, answer.swapcase()]  # Here we are return an array with all capitalize even letters and using string
    # method to convert all letters which was in uppercase to lower and lower to upper/
