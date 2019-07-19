"""
    Kata source:

        https://www.codewars.com/kata/l1-set-alarm/train/python/5d2a576f881c58001e9b6eaa

    Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever
        you are employed and the second parameter, vacation is true whenever you are on vacation.

    The function should return true if you are employed and not on vacation (because these are the circumstances
        under which you need to set an alarm). It should return false otherwise.

    Examples:

        setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) ->
              -> false setAlarm(true, false) -> true

        setalarm(true, true) -> false
        setalarm(false, true) -> false
        setalarm(false, false) -> false
        setalarm(true, false) -> true

    Sample Test:

        Test.describe("set_alarm")
        Test.it("returns correct result for all input values")
        Test.assert_equals(set_alarm(True, True), False, "Fails when input is True, True")
        Test.assert_equals(set_alarm(False, True), False, "Fails when input is False, True")
        Test.assert_equals(set_alarm(False, False), False, "Fails when input is False, False")
        Test.assert_equals(set_alarm(True, False), True, "Fails when input is True, False")
"""


def set_alarm(employed, vacation):
    # Your code here
    if employed == True and vacation == True:
        return False
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False
    elif employed == True and vacation == False:
        return True
