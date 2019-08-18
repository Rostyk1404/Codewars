"""
    Kata source :

        https://www.codewars.com/kata/count-the-smiley-faces/train/python

    Description:
        Given an array (arr) as an argument complete the function countSmileys that should return the total number of
            smiling faces.

    Rules for a smiling face:

        -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
        -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
        -Every smiling face must have a smiling mouth that should be marked with either ) or D.

    No additional characters are allowed except for those mentioned.

    Valid smiley face examples:
        :) :D ;-D :~)
        Invalid smiley faces:
        ;( :> :} :]

    Example cases:

        countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
        countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
        countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

    Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array).
        Order of the face (eyes, nose, mouth) elements will always be the same

    Happy coding!

    Sample Tests :

        Test.describe("Basic tests")
        Test.assert_equals(count_smileys([]), 0)
        Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
        Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
        Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
"""

import re


def count_smileys(arr):
    # the number of valid smiley faces in array/list
    return re.findall("[:;][-~]?[)D]", str(arr))


def count_smileys(arr):
    eyes = [":", ";"]
    nose = ["", "-", "~"]
    smile = [")", "D"]
    count = 0
    for e in eyes:
        for n in nose:
            for s in smile:
                face = e + n + s
                count += arr.count(face)
    return count


def count_smileys(arr):
    possible_variants = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D"
    return len([x for x in arr if x in possible_variants.split()])
