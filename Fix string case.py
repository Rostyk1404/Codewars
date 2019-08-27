"""
    Kata source :

        https://www.codewars.com/kata/fix-string-case/train/python/5d5744312c0867d469ef3cc0

    In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to
        convert that string to either lowercase only or uppercase only based on:

            make as few changes as possible.
            if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

    For example:

        solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
        solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
        solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

    More examples in test cases. Good luck!

        Please also try:

        Simple time difference

        Simple remove duplicates

    Sample Tests :

        Test.it("Basic tests")
        Test.assert_equals(solve("code"),"code")
        Test.assert_equals(solve("CODe"),"CODE")
        Test.assert_equals(solve("COde"),"code")
        Test.assert_equals(solve("Code"),"code")
"""


def solve(s):
    return s.upper() if len([x for x in s if x.isupper()]) > len([x for x in s if x.islower()]) else s.lower()
