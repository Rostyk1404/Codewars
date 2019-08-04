"""

    Kata source :

        https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python/5d1a504052d8e100112b4dfe

    Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
        letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
            spaces. Spaces will be included only when more than one word is present.

    Examples:

        spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

        spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=>
            returns "This is rehtona test"

    Sample Tests:

        test.assert_equals(spin_words("Welcome"), "emocleW")
"""


def spin_words(sentence):
    new_list = []
    for x in sentence.split(" "):
        if len(x) >= 5:
            new_list.append(x[::-1])
        else:
            new_list.append(x)
    return " ".join(new_list)
