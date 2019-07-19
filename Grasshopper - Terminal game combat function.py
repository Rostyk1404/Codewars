"""
    Kata source:

        https://www.codewars.com/kata/grasshopper-terminal-game-combat-function-1/train/python

    Create a combat function that takes the player's current health and the amount of damage recieved, and returns
        the player's new health. Health can't be less than 0.

    Sample Test:

        test.describe('Basic Tests')
        test.assert_equals(combat(100, 5), 95)
        test.assert_equals(combat(83, 16), 67)
        test.assert_equals(combat(20, 30), 0)

"""


def combat(health, damage):
    # your code here
    new_health = health - damage

    if new_health < 0:
        return 0
    return new_health
