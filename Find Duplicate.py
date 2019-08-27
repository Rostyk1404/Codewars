"""
    Kata source :

        https://www.codewars.com/kata/find-duplicate/train/python/5d63ea378f5c310011d60752

    Find (any) duplicate in an (integer) array A of length N+1, where 1 <= A[i] <= N, using linear space and time.

    Given A = [2, 3, 4, 1, 3]

        # duplicate(A) = 3

    Sample Tests :

        test.describe("Tests")
        test.it("Example")
        test.assert_equals(duplicate([2, 3, 4, 1, 3]), 3)
"""


def duplicate(A):
    """
        Find duplicate in A.
    """

    for x in A:
        if A.count(x) > 1:
            return x
