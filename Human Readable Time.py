"""
    Kata source :

        https://www.codewars.com/kata/human-readable-time/train/python/5d24b5c70fb98b84732b5ec3

    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
    format (HH:MM:SS)

        HH = hours, padded to 2 digits, range: 00 - 99
        MM = minutes, padded to 2 digits, range: 00 - 59
        SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.

    Sample Tests:
        Test.assert_equals(make_readable(0), "00:00:00")
        Test.assert_equals(make_readable(5), "00:00:05")
        Test.assert_equals(make_readable(60), "00:01:00")
        Test.assert_equals(make_readable(86399), "23:59:59")
        Test.assert_equals(make_readable(359999), "99:59:59")
"""


def make_readable(time):
    hours = time // 3600
    minutes = time // 60 % 60
    seconds = time % 60 % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(make_readable(359999))





    # Test.assert_equals(make_readable(0), "00:00:00")
    # Test.assert_equals(make_readable(5), "00:00:05")
    # Test.assert_equals(make_readable(60), "00:01:00")
    # Test.assert_equals(make_readable(86399), "23:59:59")
    # Test.assert_equals(make_readable(359999), "99:59:59")
