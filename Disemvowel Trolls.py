"""
    Kata source :

        https://www.codewars.com/kata/disemvowel-trolls/train/python/5d2772f5c1e94c001e84b958

    Trolls are attacking your comment section!

    A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
        neutralizing the threat.

    Your task is to write a function that takes a string and return a new string with all vowels removed.

    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

    Note: for this kata y isn't considered a vowel.

    Sample Tests:

        test.assert_equals(disemvowel("This website is for losers LOL!"),"Ths wbst s fr lsrs LL!")
"""


def disemvowel(string):
    new_list = "aeiou"
    new_str = ''
    for x in string:
        if x.lower not in new_list:
            new_str += x
    return new_str
