"""
    Kata source :

        https://www.codewars.com/kata/remove-first-and-last-character/train/python/5d572433262e9000146431e9

    It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a
        string. You're given one parameter, the original string. You don't have to worry with strings with less than
            two characters.

    Sample Tests :

        Test.describe("Tests")
        Test.assert_equals(remove_char('eloquent'), 'loquen')
        Test.assert_equals(remove_char('country'), 'ountr')
        Test.assert_equals(remove_char('person'), 'erso')
        Test.assert_equals(remove_char('place'), 'lac')
        Test.assert_equals(remove_char('ok'), '')
"""


def remove_char(s):
    # your code here
    return s[1:-1]
