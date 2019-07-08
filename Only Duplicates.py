"""
    Given a string, remove any characters that are unique from the string.

    Example:

        input: "abccdefee"

        output: "cceee"

    Sample Tests:

        test.describe("Basic tests")

        Test.assert_equals(only_duplicates('abccdefee'), 'cceee')
        Test.assert_equals(only_duplicates('hello'), 'll')
        Test.assert_equals(only_duplicates('colloquial'), 'ollol')
        Test.assert_equals(only_duplicates('foundersandcoders'), 'ondersndoders')
        Test.assert_equals(only_duplicates('12314256aaeff'), '1212aaff')
"""


def only_duplicates(string):
    return ''.join(x for x in string if string.count(x) > 1)
