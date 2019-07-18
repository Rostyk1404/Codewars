"""
    Kata source:

        https://www.codewars.com/kata/flatten-and-sort-an-array/train/python/5d2772833814220028b5615c

    Challenge:

        Given a two-dimensional array of integers, return the flattened version of the array with all the integers in
        the sorted (ascending) order.

    Example:

        Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

    Addendum:

        Please, keep in mind, that JavaScript is by default sorting objects alphabetically.
            For more information, please consult:

    http://stackoverflow.com/questions/6093874/why-doesnt-the-sort-function-of-javascript-work-well

    Sample Tests:

    Test.it("should work for some simple example test cases")
    test.assert_equals(flatten_and_sort([]), [])
    test.assert_equals(flatten_and_sort([[], [1]]), [1])
    test.assert_equals(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    test.assert_equals(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])
"""


def flatten_and_sort(array):
    return list(sorted(x for x in array if x in x))
