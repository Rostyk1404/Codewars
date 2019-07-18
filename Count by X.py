"""
    Kata source :

        https://www.codewars.com/kata/count-by-x/train/python/5d2767e730ccfb002035d735

    Create a function with two arguments that will return a list of length (n) with multiples of (x).

    Assume both the given number and the number of times to count will be positive numbers greater than 0.

    Return the results as an array (or list in Python, Haskell or Elixir).

    Examples:

        count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
        count_by(2,5) #should return [2,4,6,8,10]

    Sample Tests:

        test.assert_equals(count_by(1, 5), [1, 2, 3, 4, 5])
        test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
        test.assert_equals(count_by(3, 5), [3, 6, 9, 12, 15])
        test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
        test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])
"""


def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return list(x * y for y in range(1, n + 1))
