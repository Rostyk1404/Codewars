"""
    Kata source :

        https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/python/5d56846f52e1b1001572f4f4

    If you can't sleep, just count sheep!!

    Task:

    Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
        Input will always be valid, i.e. no negative integers.

    Sample Test :

        Test.assert_equals(count_sheep(1), "1 sheep...");
        Test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
        Test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
"""


def count_sheep(n):
    # your code
    new_list = []
    for x in range(1, n + 1):
        new_list.extend(str(x) + " " + "sheep...")
    return "".join(new_list)
