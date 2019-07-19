"""
    Kata source:

        https://www.codewars.com/kata/grouped-by-commas/train/python/5d2a7da1064c5b001713379a

    Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation
        of the number grouped by commas after every 3 digits.

    Assume:

        0 <= n < 2147483647

    Examples
               1  ->           "1"
              10  ->          "10"
             100  ->         "100"
            1000  ->       "1,000"
           10000  ->      "10,000"
          100000  ->     "100,000"
         1000000  ->   "1,000,000"
        35235235  ->  "35,235,235"

    Sample Test:

        test.assert_equals(group_by_commas(1), '1')
        test.assert_equals(group_by_commas(10), '10')
        test.assert_equals(group_by_commas(100), '100')
        test.assert_equals(group_by_commas(1000), '1,000')
        test.assert_equals(group_by_commas(10000), '10,000')
        test.assert_equals(group_by_commas(100000), '100,000')
        test.assert_equals(group_by_commas(1000000), '1,000,000')
        test.assert_equals(group_by_commas(35235235), '35,235,235')

"""

def group_by_commas(n):
    #your code here
    return "{:,}".format(n)