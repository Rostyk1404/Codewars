"""
    Kata source :

        https://www.codewars.com/kata/international-morse-code-encryption/train/python/5d3446839bcee7002ba51a2b

    Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will
        be strings.

    Characters should be separated by a single space. Words should be separated by a triple space.

    For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

    To find out more about Morse Code follow this link: https://en.wikipedia.org/wiki/Morse_code

    A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code.

    Sample Tests:

        Test.assert_equals(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        Test.assert_equals(encryption("SOS"), "... --- ...")
        Test.assert_equals(encryption("1836"), ".---- ---.. ...-- -....")
        Test.assert_equals(encryption("THE QUICK BROWN FOX"),
                "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
        Test.assert_equals(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .")
"""


# CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    morse_code = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', ' ': ' '}

    return " ".join([morse_code[x] for x in string.upper()])
