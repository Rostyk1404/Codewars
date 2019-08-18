"""
    Kata source :

        https://www.codewars.com/kata/master-of-files/train/python/5d4efece04caea000f41a345

    Are you a file extension master? Let's find out by checking if Bill's files are images or audio files. Please use
        regex if available natively for your language.

    You will create 2 string methods:

        isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible),
            with the extension .mp3, .flac, .alac, or .aac.

        isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the
            extension .jpg, .jpeg, .png, .bmp, or .gif.

    Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only.
        Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

    Rules

        It should return true or false, simply.
        File extensions should consist of lowercase letters and numbers only.
        File names should consist of letters only (uppercase, lowercase, or both)

    Good luck!

    Sample Tests :

        Test.describe("Basic tests")
        Test.assert_equals(is_audio("Nothing Else Matters.mp3"), False)
        Test.assert_equals(is_audio("NothingElseMatters.mp3"), True)
        Test.assert_equals(is_audio("DaftPunk.FLAC"), False)
        Test.assert_equals(is_audio("DaftPunk.flac"), True)
        Test.assert_equals(is_audio("AmonTobin.aac"), True)
        Test.assert_equals(is_audio(" Amon Tobin.alac"), False)
        Test.assert_equals(is_audio("tobin.alac"), True)
        Test.assert_equals(is_img("Home.jpg"), True)
        Test.assert_equals(is_img("flat.jpeg"), True)
        Test.assert_equals(is_img("icon.bmp"), True)
        Test.assert_equals(is_img("icon2.jpg"), False)
        Test.assert_equals(is_img("bounce.gif"), True)
        Test.assert_equals(is_img("animate bounce.GIF"), False)
        Test.assert_equals(is_img("transparency.png"), True)
"""


def is_audio(file_name):
    # your code here
    start, end = file_name.split(".")
    return bool(start.isalpha() and end in {'mp3', 'flac', 'aac', 'alac'})


def is_img(file_name):
    # your code here
    start, end = file_name.split(".")
    return True if start.isalpha() and end in {'jpg', 'jpeg', 'png', 'gif', 'bmp'} else False
