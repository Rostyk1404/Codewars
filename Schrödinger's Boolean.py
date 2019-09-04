"""
    Kata source :

        https://www.codewars.com/kata/schrodingers-boolean/train/python/5d572708e48e13a62d1660aa

    Can a value be both True and False?

    Define omnibool so that it returns True for the following:

        omnibool == True and omnibool == False

    If you enjoyed this kata, be sure to check out my other katas.

    Sample Tests:

        test.describe('Basic Tests')
        test.expect(omnibool == True)
        test.expect(omnibool == False)
        print('<COMPLETEDIN::>')
"""


class Schrödingers_Boolean:
    def __eq__(self, other):
        if other is True or other is False:
            return True


omnibool = Schrödingers_Boolean()
