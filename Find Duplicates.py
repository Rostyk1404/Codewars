"""
    Kata source :

        https://www.codewars.com/kata/find-duplicates/train/python/5d66d5ae189b220016fe1616

    Given an array, find the duplicates in that array, and return a new array of those duplicates. The elements of the
        returned array should appear in the order when they first appeared as duplicates.

    Note: numbers and their corresponding string representations should not be treated as duplicates
        (i.e., '1' !== 1).

    Examples

        [1, 2, 4, 4, 3, 3, 1, 5, 3, '5']  ==>  [4, 3, 1]
        [0, 1, 2, 3, 4, 5]                ==>  []

    Sample Tests:

        Test.assert_equals(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])
        Test.assert_equals(duplicates([0, 1, 2, 3, 4, 5]), [])
"""


def duplicates(array):
    dub = []
    for i, x in enumerate(array):
        if i != array.index(x) and x not in dub:
            dub.append(x)
    return dub
