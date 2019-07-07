"""
    Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.

    Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock,
    and 12:00:00 on a 24-hour clock

    Sample Input: 07:05:45PM Sample Output: 19:05:45

    Try not to use built in DateTime libraries.

    For more information on military time, check the wiki https://en.wikipedia.org/wiki/24-hour_clock#Military_time

    Sample Tests:

    Test.assert_equals(get_military_time('12:00:01AM'), '00:00:01')
    Test.assert_equals(get_military_time('11:46:47PM'), '23:46:47')
"""

from datetime import datetime


def get_military_time(time):
    return datetime.strptime(time, "%I:%M:%S%p").strftime("%H:%M:%S")


def get_military_time(time):
    if time[:2] == "12" and time[-2:] == "AM":
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[:2] == "12" and time[-2:] == "PM":
        return time[:-2]
    else:
        return str(int(time[2:]) + 12) + time[2:8]
