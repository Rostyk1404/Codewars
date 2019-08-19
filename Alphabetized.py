"""
    Kata source :

        https://www.codewars.com/kata/alphabetized/train/python/5d2fab65b7ae8800298fbad3

    The alphabetized kata

        Re-order the characters of a string, so that they are concatenated into a new string in
            "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply
                be removed!

    The input is restricted to contain no numerals and only words containing the english alphabet letters.

    Example:

        alphabetized("The Holy Bible") # "BbeehHilloTy"

    Inspired by Tauba Auerbach

    Sample Tests :

        Test.describe("Basic tests")
        Test.assert_equals(alphabetized(""), "")
        Test.assert_equals(alphabetized(" "), "")
        Test.assert_equals(alphabetized(" a"), "a")
        Test.assert_equals(alphabetized("a "), "a")
        Test.assert_equals(alphabetized(" a "), "a")
        Test.assert_equals(alphabetized("A b B a"), "AabB")
        Test.assert_equals(alphabetized(" a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"), "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ")
        Test.assert_equals(alphabetized("!@$%^&*()_+=-`,"), "")
        Test.assert_equals(alphabetized("The Holy Bible"), "BbeehHilloTy")
        Test.assert_equals(alphabetized("CodeWars can't Load Today"), "aaaaCcdddeLnooorstTWy")
        print("<COMPLETEDIN::>")
"""


def alphabetized(s):
    # your code here
    return "".join(sorted([x for x in s if x.isalpha()], key=lambda x: x.lower()))
