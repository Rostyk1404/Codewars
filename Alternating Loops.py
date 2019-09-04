"""
    Kata source :

      https://www.codewars.com/kata/alternating-loops/train/python

    Write function combine() that combines arrays by alternatingly taking elements passed to it.

    E.g

        combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
        combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
        combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]

    Arrays can have different lengths.

    Sample Tests :

        Test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3]), ['a', 1, 'b', 2, 'c', 3])
        Test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]), ['a', 1, 'b', 2, 'c', 3, 4, 5])
        Test.assert_equals(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]),
            ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
        Test.assert_equals(combine([{ 'a': 1 }, { 'b': 2 }], [1, 2]),[{"a":1},1,{"b":2},2])
        Test.assert_equals(combine([{ 'a': 2, 'b':1 }, { 'a': 1, 'b': 2 }], [1, 2, 3, 4],[5,6],[7]),
            [{"a":2,"b":1},1,5,7,{"a":1,"b":2},2,6,3,4])
"""


def combine(*args):
    # your code here
    new_list = []
    max_length = max([len(lst) for lst in args])
    for x in range(max_length):
        for lst in list(args):
            if len(lst) > x:
                new_list.append(lst[x])
    return new_list


print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]))
