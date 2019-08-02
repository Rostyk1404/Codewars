"""
    Kata source :

        https://www.codewars.com/kata/morse-code-translate-text-to-and-from-morse-code/train/python/5d339aa771baf7000d144937

    Morse Code was a way early telecommunication method. It was a simple translation of alpha numeric characters to a
        series of short and long signals often described as dot and dashes (. -). This kata will have you take text and
            transform it to a series of dots and dashes, as well as taking a series of dots and dashes into text.
                Solving this kata can expose you to the various functions in each language such as:

    Strings,Arrays,Loops,Regular Expressions,Splitting/Joining/Replacing Strings.

    Below are the characters and their associated morse code:

        https://imgur.com/xMAVxAC

    Please note that morse code does not have separate codes for upper and lower case. For this challenge you should
        assume all text to be in lower case.

    To clarify both "(" and ")" are the same sequence in morse code "-.--.-". when translating back from morse code to
        text either will be acceptable.

    Arrays/Lists/Hashes/Objects/Sequences for both "morse code -> character" and "character -> morse" code are preloaded
        and may be accessed as such:

              textToMorse["a"]
              morseToText[".-"]

    In python arrays are created and used like this:

              myarray={}
              myarray=["a"] = "0"
              print(myarray["a"]) -> 0

              myarray=["a","b","c"]
              print(myarray[0]) -> a

    Sample Tests:

        test.describe("Translate To Morse");
        test.expect('.... . .-.. .-.. --- / .-- --- .-. .-.. -..' == translateToMorse('Hello World'))

        test.describe("TranSample Tests:slate To Text");
        test.expect('hello world' == translateToText('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'))
"""
morse_code = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '-...': 'b',
              '-..-': 'x', '.-.': 'r', '.--': 'w', '..---': '2', '.-': 'a', '..': 'i', '..-.': 'f', '.': 'e',
              '.-..': 'l', '...': 's', '..-': 'u', '..--..': '?', '.----': '1', '-.-': 'k', '-..': 'd',
              '-....': '6', '-...-': '=', '---': 'o', '.--.': 'p', '.-.-.-': '.', '--': 'm', '-.': 'n', '....': 'h',
              '.----.': "'", '...-': 'v', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')',
              '-.-.--': '!', '--.': 'g', '--.-': 'q', '--..': 'z', '-..-.': '/', '.-.-.': '+', '-.-.': 'c',
              '---...': ':', '-.--': 'y', '-': 't', '.--.-.': '@', '...-..-': '$', '.---': 'j', '-----': '0',
              '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3', '/': ' '}

translate_To_Morse = {v: k for k, v in morse_code.items()}


def translateToMorse(text):
    return ' '.join(translate_To_Morse[x] for x in text.lower())


def translateToText(morse):
    return "".join(morse_code[x.capitalize()] for x in morse.split())
