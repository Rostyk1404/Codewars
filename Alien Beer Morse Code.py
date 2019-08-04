"""
    Kata source:

        https://www.codewars.com/kata/alien-beer-morse-code/train/python/5d339a6de3ab930019b125b3

    The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply
        the exact number of beers demanded.

    Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the
        following convention:

            1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----

    Sample Tests:

        Test.describe("Basic tests")
        Test.assert_equals(morse_converter(".----"), 1)
        Test.assert_equals(morse_converter("..----------..."), 207)
        Test.assert_equals(morse_converter("----.--.....---...--"), 9723)

"""


def morse_converter(string):
    # The survival of Earth depends on your code!

    morse_code = {"-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                  ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}

    return int("".join(morse_code[string[x:x + 5]] for x in range(0, len(string), 5)))
