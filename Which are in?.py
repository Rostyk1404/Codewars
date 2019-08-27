"""
    Kata source :

        https://www.codewars.com/kata/which-are-in/train/python/5d1a9e660e313ea65c557dbb

    Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which
        are substrings of strings of a2.

    #Example 1:

        a1 = ["arp", "live", "strong"]

        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    returns ["arp", "live", "strong"]

    #Example 2:

        a1 = ["tarp", "mice", "bull"]

        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    returns []

    Notes:

        Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

        In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

        Beware: r must be without duplicates.

        Don't mutate the inputs.

    Sample Tests :

        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']

        test.assert_equals(in_array(a1, a2), r)
"""


def in_array(array1, array2):
    # your code
    new_list = []
    for x in array1:
        for y in array2:
            if x in y not in new_list:
                new_list.append(x)
    return sorted(set(new_list))
