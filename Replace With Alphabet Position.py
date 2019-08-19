"""
    Kata source :

        https://www.codewars.com/kata/replace-with-alphabet-position/train/python/5d24589e2cf4820015c59370

    Welcome.

    In this kata you are required to, given a string, replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.

    "a" = 1, "b" = 2, etc.

    Example

        alphabet_position("The sunset sets at twelve o' clock.")

    Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

    Sample Tests:
        from random import randint
        test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."),
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        test.assert_equals(alphabet_position("The narwhal bacons at midnight."),
            "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        test.assert_equals(alphabet_position(number_test), "")
"""


def alphabet_position(text):
    dic = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
           'k': '11', 'l': '12', 'm': '13',
           'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
           'x': '24', 'y': '25', 'z': '26'}
    new_list = []  # creating new list in which we will append result
    for x in text.lower():  # changing all x(letters) to lower case
        for k, v in dic.items():  # searching an elements
            if k == x:  # checking if key is same a x
                new_list.append(v)  # if same we will append value (numbers) in list
    return " ".join(new_list)  # converting list to string and adding spaces between number

