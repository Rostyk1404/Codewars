"""
    You are given array of integers, your task will be to count all pairs in that array and return their count.

    Notes:

    Array can be empty or contain only one value; in this case return 0
    If there are more pairs of a certain number, count each pair only once. E.g.: for [0, 0, 0, 0]
    the return value is 2 (= 2 pairs of 0s)
    Random tests: maximum array length is 1000, range of values in array is between 0 and 1000

    Sample Tests:

        test.assert_equals(duplicates([1, 2, 5, 6, 5, 2]) , 2)
        test.assert_equals(duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]), 4)
        test.assert_equals(duplicates([0, 0, 0, 0, 0, 0, 0]) , 3)
        test.assert_equals(duplicates([1000, 1000]), 1)
        test.assert_equals(duplicates([]), 0)
        test.assert_equals(duplicates([54]), 0)

"""


def duplicates(arr):
    return sum([arr.count(x) // 2 for x in set(arr)])
