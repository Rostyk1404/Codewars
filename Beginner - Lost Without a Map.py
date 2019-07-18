"""
    Kata source :

        https://www.codewars.com/kata/beginner-lost-without-a-map/train/python/5d28935bf9092c002b8a576b

    Given an array of integers, return a new array with each value doubled.

    For example:

        [1, 2, 3] --> [2, 4, 6]

    For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

    Sample Test :

        test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
        test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        test.assert_equals(maps([]), [])
"""


def maps(a):
    return list(map(lambda x: x * 2, a))
