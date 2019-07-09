"""
    Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

    Example:
        ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

    Sample Tests:
        test.describe("Basic Tests")

        tests = (
            ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
            ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
    )

    for t in tests:
        inp, exp = t
        test.assert_equals(ordered_count(inp), exp)
"""


def ordered_count(input):
    extra_list = []
    new_list = []

    for x in list(input):
        if x not in extra_list:
            new_list.append((x, input.count(x)))
            extra_list.append(x)
    return new_list
