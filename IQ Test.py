"""
    Kata source :

        https://www.codewars.com/kata/iq-test/train/python

    Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
        differs from the others. Bob observed that one number usually differs from the others in evenness.
    Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in
        evenness, and return a position of this number.! Keep in mind that your task is to help \
    Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

    Examples :

        iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

        iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

    Sample Tests:

        Test.assert_equals(iq_test("2 4 7 8 10"),3)
        Test.assert_equals(iq_test("1 2 2"), 1)
"""


def iq_test(numbers):
    # your code here
    even = [int(x) % 2 == 0 for x in numbers.split()]
    return even.index(True) + 1 if even.count(True) == 1 else even.index(False) + 1