"""
    Kata source :

        https://www.codewars.com/kata/friend-or-foe/train/python

    Make a program that filters a list of strings and returns a list with only your friends name in it.

    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise,
        you can be sure he's not...

    Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

    i.e.

        friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

    Note: keep the original order of the names in the output.

    Sample Test :

        Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])

"""


def friend(x):
    # Code
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list
