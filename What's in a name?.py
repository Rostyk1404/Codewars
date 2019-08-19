"""
    Kata source :

        https://www.codewars.com/kata/whats-in-a-name/train/python/5d56d58d90b243002b51b236

    What's in a name?

        ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.

    Task

        Test whether or not the string contains all of the letters which spell a given name, in order.

    The format

        A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name)
            { return true || false }``

        Examples
        nameInStr('Across the rivers', 'chris') --> true
                    ^      ^  ^^   ^
                    c      h  ri   s

        Contains all of the letters in 'chris', in order.
            nameInStr('Next to a lake', 'chris') --> false

        Contains none of the letters in 'chris'.
            nameInStr('Under a sea', 'chris') --> false
                       ^   ^
                       r   s

        Contains only some of the letters in 'chris'.
            nameInStr('A crew that boards the ship', 'chris') --> false
                     cr    h              s i
                     cr                h  s i
                     c     h      r       s i
                     ...

        Contains all of the letters in 'chris', but not in order.
            nameInStr('A live son', 'Allison') --> false
                   ^ ^^   ^^^
                   A li   son

        Contains all of the correct letters in 'Allison', in order,
            but not enough of all of them (missing an 'l').

    Note: testing will not be case-sensative.

    Sample Tests :

        Test.describe("Basic tests")
        Test.assert_equals(name_in_str("Across the rivers", "chris"), True)
        Test.assert_equals(name_in_str("Next to a lake", "chris"), False)
        Test.assert_equals(name_in_str("Under a sea", "chris"), False)
        Test.assert_equals(name_in_str("A crew that boards the ship", "chris"), False)
        Test.assert_equals(name_in_str("A live son", "Allison"), False)
        Test.assert_equals(name_in_str("Just enough nice friends","Jennifer"),False)
        Test.assert_equals(name_in_str("thomas","Thomas"),True)
        Test.assert_equals(name_in_str("pippippi","Pippi"),True)
        Test.assert_equals(name_in_str("pipipp","Pippi"),False)
        Test.assert_equals(name_in_str("ppipip","Pippi"),False)
"""


def name_in_str(str, name):
    # your code here
    string = iter(str.lower())  # iter will remove all past elements
    return all(
        x in string for x in name.lower())  # method all will return True only if all x(letters) will be in name if
    # other case False
