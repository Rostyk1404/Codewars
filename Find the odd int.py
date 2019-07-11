"""
    Kata source :

        https://www.codewars.com/kata/find-the-odd-int/train/python

    Given an array, find the int that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.

    Sample Tests:

        test.describe("Example")
        test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

"""


def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 != 0:
            return x
