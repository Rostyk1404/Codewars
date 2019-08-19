"""
    Kata source :

        https://www.codewars.com/kata/anagram-difference/train/python

    Given two words, how many letters do you have to remove from them to make them anagrams?

    Example
        First word : c od e w ar s (4 letters removed)
        Second word : ha c k er r a nk (6 letters removed)
        Result : 10

    Hints
        A word is an anagram of another word if they have the same letters (usually in a different order).
        Do not worry about case. All inputs will be lowercase.
        When you're done with this kata, check out its big brother/sister :
            https://www.codewars.com/kata/hardcore-anagram-difference

    Sample Tests:

        test_cases = (
        ('', '', 0),
        ('a', '', 1),
        ('', 'a', 1),
        ('ab', 'a', 1),
        ('ab', 'ba', 0),
        ('ab', 'cd', 4),
        ('codewars', 'hackerrank', 10)
        )

    for first_word, second_word, expected in test_cases:

        test.assert_equals(anagram_difference(first_word, second_word), expected)
"""


def anagram_difference(w1, w2):
    # the number of characters to remove from w1 and w2 to make them anagrams of each other
    return sum(abs(w1.count(x) - w2.count(x)) for x in set(w1 + w2))  # we are using function abs only because that can
    # be some negative values
