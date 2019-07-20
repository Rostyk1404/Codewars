"""
    Kata source :

        https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

    Part of Series 1/3
        This kata is part of a series on the Morse code. After you solve this kata, you may move to
            the [next one](/kata/decode-the-morse-code-advanced).

    In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice
        and digital data communication channels, it still has its use in some applications around the world.

    The Morse code encodes every character as a sequence of "dots" and "dashes".
        For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
        The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in
        Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words.

    For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

    NOTE: Extra spaces before or after the code have no meaning and should be ignored.

    In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of
        those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···.
            These special codes are treated as single special characters, and usually are transmitted as separate words.

    Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

    For example:

        decodeMorse('.... . -.--   .--- ..- -.. .')

            #should return "HEY JUDE"

    NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

    The Morse code table is preloaded for you as a dictionary, feel free to use it:

        Coffeescript/C++/Go/JavaScript/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
        C#: MorseCode.Get(".--") (returns string)
        Elixir: morse_codes variable
        Elm: MorseCodes.get : Dict String String
        Haskell: morseCodes ! ".--" (Codes are in a Map String String)
        Java: MorseCode.get(".--")
        Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
        Rust: self.morse_code
        Scala: morseCodes(".--")
        All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions.
        In C#, tests will fail if the solution code throws an exception, please keep that in mind.
        This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

    Good luck!

    After you complete this kata, you may try yourself at Decode the Morse code, advanced.

    Sample Tests:

        def test_and_print(got, expected):
            if got == expected:
                test.expect(True)
            else:
                print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
                test.expect(False)

        test.describe("Example from description")
        test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

        test.describe("Your own tests")
        # Add more tests here
"""


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message

    MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4',
                  '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X',
                  '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I',
                  '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U',
                  '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6',
                  '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
                  '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
                  '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
                  '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C',
                  '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$',
                  '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(',
                  '---..': '8', '...--': '3'}

    return " ".join("".join(MORSE_CODE[x] for x in word.split(" ")) for word in morse_code.strip().split("   "))
