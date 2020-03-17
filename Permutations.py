"""
    Kata source :

        https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python/5d23a6b1c193ae000dea7811

    In this kata you have to create all permutations of an input string and remove duplicates, if present.
        This means, you have to shuffle all letters from the input in all possible orders.

    Examples:
        permutations('a'); # ['a']
        permutations('ab'); # ['ab', 'ba']
        permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

    The order of the permutations doesn't matter.

    Sample Tests:
        Test.assert_equals(sorted(permutations('a')), ['a']);
        Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
        Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
"""

import itertools


def permutations(string):
    # your code here
    return list(" ".join(x) for x in set(itertools.permutations(string)))
