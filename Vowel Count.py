"""
    Kata source :

        https://www.codewars.com/kata/vowel-count/train/python

    Return the number (count) of vowels in the given string.

    We will consider a, e, i, o, and u as vowels for this Kata.

    The input string will only consist of lower case letters and/or spaces.

    Sample Tests:

        test.assert_equals(getCount("abracadabra"), 5)
"""


def getCount(inputStr):
    num_vowels = 0

    for x in inputStr.lower():
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            num_vowels += 1
    return num_vowels
