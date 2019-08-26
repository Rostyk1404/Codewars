"""
    Kata source :

        https://www.codewars.com/kata/indexed-capitalization/train/python/5d63c6bc8f5c310025d2fe4f

    Given a string and an array of integers representing indices, capitalize all letters at the given indices.

    For example:

        capitalize("abcdef",[1,2,5]) = "aBCdeF"
        capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.

    The input will be a lowercase string with no spaces and an array of digits.

    Good luck!

    Be sure to also try:

        Alternate capitalization

        String array revisal

    Sample Tests :

        Test.it("Basic tests")
        Test.assert_equals(capitalize(),'aBCdeF')
        Test.assert_equals(capitalize("abcdef",[1,2,5,100]),'aBCdeF',)
        Test.assert_equals(capitalize("codewars",[1,3,5,50]),'cOdEwArs')
        Test.assert_equals(capitalize("abracadabra",[2,6,9,10]),'abRacaDabRA')
        Test.assert_equals(capitalize("codewarriors",[5]),'codewArriors')
"""


def capitalize(s, ind):
    new_list = []
    for i,x in enumerate(s):
        if i in ind:
            new_list.append(x.capitalize())
        else:
            new_list.append(x)
    return "".join(new_list)

