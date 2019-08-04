"""
    Kata source:

        https://www.codewars.com/kata/count-odd-numbers-below-n/train/python/5d275d73c1e94c0025827bfe

    Given a number n, return the number of positive odd numbers below n, EASY!

        oddCount(7) //=> 3, i.e [1, 3, 5]
        oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

    Expect large Inputs!

    Sample Tests:

        Test.it("Basic tests")
        Test.assert_equals(odd_count(15),7)
        Test.assert_equals(odd_count(15023),7511)
"""


def odd_count(n):
    return n // 2
