"""
    Kata source:

        https://www.codewars.com/kata/detect-pangram/train/python/5d1a9c53c193ae000d9cc67d

    A pangram is a sentence that contains every single letter of the alphabet at least once.
        For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the
            letters A-Z at least once (case is irrelevant).

    Given a string, detect whether or not it is a pangram.
        Return True if it is, False if not. Ignore numbers and punctuation.

    Test sample :

        pangram = "The quick, brown fox jumps over the lazy dog!"
        Test.assert_equals(is_pangram(pangram), True)
"""


def is_pangram(s):
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in s.lower():
            return False
    return True
