"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

    - It is a concatenation of one or more words consisting of English letters.
    - All letters in the first word are lowercase.
    - For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, determine the number of words in s.
"""


def camel_case(s: str) -> int:
    """
    This function takes as an input a string (s) written in camel-case and returns an integer representing the number
    of words in s.

    Example:
        (1) s = "oneTwoThree"
            camel_case(s) => 3
    """

    number_of_words = 1
    for i in range(len(s)):
        if s[i].isupper():
            number_of_words = number_of_words + 1
    return number_of_words


# ----------------- TESTS -----------------

s_1 = "oneTwoThree"
print(camel_case(s_1))
# Expected Output: 3

s_2 = "saveChangesInTheEditor"
print(camel_case(s_2))
# Expected Output: 5

s_3 = "thereIsASequenceOfWordsInCamelCaseAsAStringOfLetters"
print(camel_case(s_3))
# Expected Output: 14
