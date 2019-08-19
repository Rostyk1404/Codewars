"""
    Kata source :

        https://www.codewars.com/kata/remove-duplicate-words/train/python

    Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

    Example:

    Input:

        'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

    Output:

        'alpha beta gamma delta'

    Sample Tests:

        Test.it("Basic tests")
        Test.assert_equals(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma
            gamma gamma delta"), "alpha beta gamma delta")
        Test.assert_equals(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
"""


def remove_duplicate_words(s):
    new_list = []  # we are creating new list in which we will append our words
    for x in s.split(" "):  # here we are spliting the word by space and saving them in x
        if x not in new_list:  # this line of code checking if x in the list or not. If it is not we will
            new_list.append(x)  # append that word into new list if the word in list we will not
    return " ".join(new_list)  # here we converting list to string via method join
