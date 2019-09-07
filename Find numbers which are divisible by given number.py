"""
    Kata source :

        https://www.codewars.com/kata/find-numbers-which-are-divisible-by-given-number/train/python

    Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
    First argument is an array of numbers and the second is the divisor.

    Example:

        divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

    Sample Tests:

        Test.describe("Fixed tests")
        Test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
        Test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
        Test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
        Test.assert_equals(divisible_by([0], 4), [0])
        Test.assert_equals(divisible_by([1,3,5], 2), [])
"""


def divisible_by(numbers, divisor):
    new_list = []
    for x in numbers:
        if x % divisor == 0:
            new_list.append(x)
    return new_list


def divisible_by(numbers, divisor):
    return list(filter(lambda x: x % divisor == 0, numbers))


def divisible_by(numbers, divisor):
    return list(x for x in numbers if x % divisor == 0)
