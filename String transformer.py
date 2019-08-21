"""
    Kata source :

        https://www.codewars.com/kata/5878520d52628a092f0002d0

    Given a string, return a new string that has transformed based on the input:

        Change case of every character, ie. lower case to upper case, upper case to lower case.
        Reverse the order of words from the input.

    Note: You will have to handle multiple spaces, and leading/trailing spaces.

    For example:

        "Example Input" ==> "iNPUT eXAMPLE"

    You may assume the input only contain English alphabet and spaces.

    Sample Tests :

        test.assert_equals(string_transformer("Example string"), "STRING eXAMPLE")
        test.assert_equals(string_transformer("Example Input"), "iNPUT eXAMPLE")
        test.assert_equals(string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")
        # Should handle empty string
        test.assert_equals(string_transformer(""), "")
        # Should handle multiple spaces
        test.assert_equals(string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU")
        # Should handle leading space
        test.assert_equals(string_transformer(" A b C d E f G "), " g F e D c B a ")
"""


def string_transformer(s):
    # your code here
    return " ".join([x.swapcase() for x in s.split(" ")[::-1]])


def string_transformer(s):
    # your code here
    new_list = []  # firstly we have to create an empty list. Latter we will append our words and letters in that list
    for x in s.split(" "):  # on this stage we are splitting our sentence and in x we are saving each letter or word
        new_list.append("".join(x.swapcase()))  # here we are changing all letters which were in upper case to
        # lower and vice versa
    return " ".join(new_list[::-1])  # here we are transform list to string and making a reverse
