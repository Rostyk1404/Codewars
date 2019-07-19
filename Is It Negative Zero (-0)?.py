"""
    Kata source:

        https://www.codewars.com/kata/is-it-negative-zero-0/train/python/5d2b614e2896d7001c3dcc86

    There exist two zeroes: +0 (or just 0) and -0.

    Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).

    In JavaScript / TypeScript / Coffeescript the input will be a number.

    In Python / Java / C / NASM / Haskell / the input will be a float.

    Sample Test:

            @test.describe('Basic Tests')

        def basic_tests():

            @test.it('should return true for -0.0 and false for all other numbers')

            def basic_test_case():

                test.assert_equals(is_negative_zero(-0.0), True)
                test.assert_equals(is_negative_zero(-(float("inf"))), False)
                test.assert_equals(is_negative_zero(-5.0), False)
                test.assert_equals(is_negative_zero(-4.0), False)
                test.assert_equals(is_negative_zero(-3.0), False)
                test.assert_equals(is_negative_zero(-2.0), False)
                test.assert_equals(is_negative_zero(-1.0), False)
                test.assert_equals(is_negative_zero(0.0), False)
                test.assert_equals(is_negative_zero(1.0), False)
                test.assert_equals(is_negative_zero(2.0), False)
                test.assert_equals(is_negative_zero(3.0), False)
                test.assert_equals(is_negative_zero(4.0), False)
                test.assert_equals(is_negative_zero(5.0), False)
                test.assert_equals(is_negative_zero(float("inf")), False)
"""


def is_negative_zero(n):
    if str(n) == "-0.0":
        return True
    return False
