"""
    Kata source :

        https://www.codewars.com/kata/sort-out-the-men-from-boys-1/train/python

    Scenario
        Now that the competition gets tough it will Sort out the men from the boys .

        Men are the Even numbers and Boys are the odd  !alt !alt

        Task
        Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the
        boys  !alt !alt

        Notes
        Return an array/list where Even numbers come first then odds

        Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .

        Array/list size is at least *4*** .

        Array/list numbers could be a mixture of positives , negatives .

        Have no fear , It is guaranteed that no Zeroes will exists . !alt

        Repetition of numbers in the array/list could occur , So (duplications are not included when separating).

    Input >> Output Examples:
        1- menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3})

    Explanation:

        Since , { -100, -96 , -94 } is the even numbers here , So it came first in ascending order ,
        *then** *the odds in descending order { -99 }

        Since , (Duplications are not included when separating) , then you can see only one (-99) was appeared in the
        final array/list .

        3- menFromBoys ({49 , 818 , -282 , 900 , 928 , 281 , -282 , -1 }) ==>
            return ({-282 , 818 , 900 , 928 , 281 , 49 , -1})

    Explanation:

        Since , {-282 , 818 , 900 , 928 } is the even numbers here , So it came first in ascending order ,
        then the odds in descending order { 281 , 49 , -1 }

        Since , (Duplications are not included when separating) , then you can see only one (-282) was appeared in the
        final array/list .

    Sample Tests:

        Test.describe("Basic tests")
        Test.assert_equals(men_from_boys([7,3,14,17]), [14,17,7,3])
        Test.assert_equals(men_from_boys([2,43,95,90,37]), [2,90,95,43,37])
        Test.assert_equals(men_from_boys([20,33,50,34,43,46]), [20,34,46,50,43,33])
        Test.assert_equals(men_from_boys([82,91,72,76,76,100,85]), [72,76,82,100,91,85])
        Test.assert_equals(men_from_boys([2,15,17,15,2,10,10,17,1,1]), [2,10,17,15,1])
        Test.assert_equals(men_from_boys([-32,-39,-35,-41]), [-32,-35,-39,-41])
        Test.assert_equals(men_from_boys([-64,-71,-63,-66,-65]), [-66,-64,-63,-65,-71])
        Test.assert_equals(men_from_boys([-94,-99,-100,-99,-96,-99]), [-100,-96,-94,-99])
        Test.assert_equals(men_from_boys([-53,-26,-53,-27,-49,-51,-14]), [-26,-14,-27,-49,-51,-53])
        Test.assert_equals(men_from_boys([-17,-45,-15,-33,-85,-56,-86,-30]), [-86,-56,-30,-15,-17,-33,-45,-85])
        Test.assert_equals(men_from_boys([12,89,-38,-78]), [-78,-38,12,89])
        Test.assert_equals(men_from_boys([2,-43,95,-90,37]), [-90,2,95,37,-43])
        Test.assert_equals(men_from_boys([82,-61,-87,-12,21,1]), [-12,82,21,1,-61,-87])
        Test.assert_equals(men_from_boys([63,-57,76,-85,88,2,-28]), [-28,2,76,88,63,-57,-85])
        Test.assert_equals(men_from_boys([49,818,-282,900,928,281,-282,-1]), [-282,818,900,928,281,49,-1])
        print("<COMPLETEDIN::>")
"""


def men_from_boys(arr):
    return sorted(set([x for x in arr if x % 2 == 0])) + sorted(set([x for x in arr if x % 2 != 0]))[::-1]
