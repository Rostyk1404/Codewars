"""
    Kata source :

        https://www.codewars.com/kata/weird-string-case/train/python

    Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even
        indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
            The indexing just explained is zero based, so the zero-ith index is even, therefore that character should
                be upper cased.

    The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if
        there are multiple words. Words will be separated by a single space(' ').

    Examples:

        to_weird_case('String'); # => returns 'StRiNg'
        to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

    Sample Test :

        test.describe('to_weird_case')

        test.it('should return the correct value for a single word')
        test.assert_equals(to_weird_case('This'), 'ThIs')
        test.assert_equals(to_weird_case('is'), 'Is')

        test.it('should return the correct value for multiple words')
        test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
"""


def to_weird_case(string):
    # TODO
    return " ".join(
        "".join(x.capitalize() if i % 2 == 0 else x for i, x in enumerate(word)) for word in
        string.split(" "))  # method
    # capitalize "in other way u can use upper" with transform all even letters in uppercase then u have to use
    # enumerate which will numerate a letters form 0 to the end of the sentence but firstly we have to split current
    # sentence because every new word in sentence after "space" must start with 0.
