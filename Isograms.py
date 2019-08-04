"""
    Kata source :

        https://www.codewars.com/kata/isograms/train/python/5d27640ac85023000f8cce53

    An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
        determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
            Ignore letter case.

                is_isogram("Dermatoglyphics" ) == true
                is_isogram("aba" ) == false
                is_isogram("moOse" ) == false # -- ignore letter case

    Sample Tests:

        Test.assert_equals(is_isogram("Dermatoglyphics"), True )
        Test.assert_equals(is_isogram("isogram"), True )
        Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
        Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
        Test.assert_equals(is_isogram("isIsogram"), False )
        Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )
"""


def is_isogram(string):
    for x in string.lower():
        if string.lower().count(x) > 1:
            return False
    return True
