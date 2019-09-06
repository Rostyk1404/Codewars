"""
    Kata source :

        https://www.codewars.com/kata/a-needle-in-the-haystack/train/python/5d7247c89a15b50025f6ebd4

    Can you find the needle in the haystack?

    Write a function findNeedle() that takes an array full of junk but containing one "needle"

    After your function finds the needle it should return a message (as a string) that says:

        "found the needle at position " plus the index it found the needle, so:

        find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])

        should return "found the needle at position 5"

    Sample Tests :

        def run_test(arr, n, s=''): test.assert_equals(find_needle(arr), 'found the needle at position %d' % n, s)

            run_test(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False], 3)

            run_test(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle',
                'something somebody lost a while ago'], 5)

            run_test([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',
                1,2,3,4,5,5,6,5,4,32,3,45,54], 30)
"""


def find_needle(haystack):
    # your code here
    for i, x in enumerate(haystack):
        if x is "needle":
            return f"found the needle at position {i}"


def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
