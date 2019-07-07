"""
    Find the 2nd largest integer in array If the array has no 2nd largest integer then return nil. Reject all non
    integers elements and then find the 2nd largest integer in array

    find_2nd_largest([1,2,3]) => 2

    find_2nd_largest([1,1,1,1,1]) => nil because all elements are same. Largest no. is 1. and there is no 2nd largest no.

    find_2nd_largest([1,'a','2',3,3,4,5,'b']) => 4 as after rejecting non integers array will be [1,3,3,4,5] Largest no.
    is 5. and 2nd largest is 4.

    Return nil if there is no 2nd largest integer. Take care of big numbers as well

    Sample Tests:

    test.describe("Example Tests")
    test.assert_equals(find_2nd_largest([1,2,3]), 2)
    test.assert_equals(find_2nd_largest([1,1,1,1,1,1,1]), None)
    test.assert_equals(find_2nd_largest([1,'a','2',3,3,4,5,'b']),4)
    test.assert_equals(find_2nd_largest([1,'a','2',3,3,3333333333333333333334,
    544444444444444444444444444444,'b']),3333333333333333333334)
"""


def find_2nd_largest(arr):
    new_list = []
    for x in set(arr):
        if isinstance(x, int):
            new_list.append(x)
    return sorted(new_list)[-2] if len(new_list) > 1 else None
