"""
    Kata source :

        https://www.codewars.com/kata/surface-area-and-volume-of-a-box/train/python/5d276b22c85023000f8d021b

    Write a function that returns the total surface area and volume of a box as an array: [area, volume]

    Sample Tests:

        Test.assert_equals(get_size(4, 2, 6), [88,48])
        Test.assert_equals(get_size(1, 1, 1), [6,1])
        Test.assert_equals(get_size(1, 2, 1), [10,2])
        Test.assert_equals(get_size(1, 2, 2), [16,4])
        Test.assert_equals(get_size(10, 10, 10), [600,1000])
"""


def get_size(w, h, d):
    return [2 * (w * h) + 2 * (w * d) + 2 * (h * d), w * h * d]
