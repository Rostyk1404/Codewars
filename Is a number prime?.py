"""
    Kata source :

        https://www.codewars.com/kata/is-a-number-prime/train/python/5d29cce540459900154812ae

    Define a function that takes an integer argument and returns logical value true or false depending on if the integer
        is a prime.

    Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other
        than 1 and itself.

    Example

        is_prime(1)  /* false */
        is_prime(2)  /* true  */
        is_prime(-1) /* false */

    Assumptions

        You can assume you will be given an integer input.

        You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).

        There are no fancy optimizations required, but still the most trivial solutions might time out. Try to find a
            solution which does not loop all the way up to n.

    Sample Tests :

        @Test.describe("Basic")

        def basic():

            @Test.it("Basic tests")
            def basic_tests():
                Test.assert_equals(is_prime(0),  False, "0  is not prime")
                Test.assert_equals(is_prime(1),  False, "1  is not prime")
                Test.assert_equals(is_prime(2),  True, "2  is prime")
                Test.assert_equals(is_prime(73), True, "73 is prime")
                Test.assert_equals(is_prime(75), False, "75 is not prime")
                Test.assert_equals(is_prime(-1), False, "-1 is not prime")


            @Test.it("Test prime")
            def test_prime():
                Test.assert_equals(is_prime(3),  True, "3  is not prime");
                Test.assert_equals(is_prime(5),  True, "5  is not prime");
                Test.assert_equals(is_prime(7),  True, "7  is prime");
                Test.assert_equals(is_prime(41), True, "41 is prime");
                Test.assert_equals(is_prime(5099), True, "5099 is prime");

            @Test.it("Test not prime")
            def test_not_prime():
                Test.assert_equals(is_prime(4),  False, "4  is not prime");
                Test.assert_equals(is_prime(6),  False, "6  is not prime");
                Test.assert_equals(is_prime(8),  False, "8  is prime");
                Test.assert_equals(is_prime(9), False, "9 is prime");
                Test.assert_equals(is_prime(45), False, "45 is not prime");
                Test.assert_equals(is_prime(-5), False, "-5 is not prime");
                Test.assert_equals(is_prime(-8), False, "-8 is not prime");
                Test.assert_equals(is_prime(-41), False, "-41 is not prime");
"""


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def is_prime(n):
    return n > 1 and not any(n % x == 0 for x in range(2, n))
