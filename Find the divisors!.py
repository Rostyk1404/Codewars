"""
    Kata source :

        https://www.codewars.com/kata/find-the-divisors/train/python/5d27613df9092c000f7b8d43

    Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the
        integer's divisors(except for 1 and the number itself), from smallest to largest.
            If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell
                and Result<Vec<u32>, String> in Rust).

    Example:

        divisors(12); #should return [2,3,4,6]
        divisors(25); #should return [5]
        divisors(13); #should return "13 is prime"

    Sample Tests :

        Test.assert_equals(divisors(15), [3, 5]);
        Test.assert_equals(divisors(12), [2, 3, 4, 6]);
        Test.assert_equals(divisors(13), "13 is prime");
"""


def divisors(integer):
    return list(x for x in range(2, integer) if integer % x == 0) or f"{integer} is prime"
