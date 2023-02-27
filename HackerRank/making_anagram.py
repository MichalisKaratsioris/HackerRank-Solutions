"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each
other if the first string's letters can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency. For example, "bacdc" and "dcbac" are anagrams, but
"bacdc" and "dcbad" are not. The student decides on an encryption scheme that involves two large strings. The
encryption is dependent on the minimum number of character deletions required to make the two strings anagrams.
Determine this number.

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
"""


def making_anagram(a: str, b: str) -> int:
    """
    This function takes as an input two string, a and b, and returns an integer representing the minimum character
    deletion the function applies so that the resulting strings are anagrams.

    Example:
        (1) a = "bacdc"
            b = "dcbac"
            making_anagram(a, b) => 0
    """

    diff = 0
    a_arr = []
    b_arr = []
    for i in range(len(a)):
        a_arr.append(a[i])
    for i in range(len(b)):
        b_arr.append(b[i])
    a_set = set(a_arr)
    b_set = set(b_arr)
    a_dic = {}
    b_dic = {}
    for c in a_set:
        a_dic[c] = 0
    for c in b_set:
        b_dic[c] = 0
    for c in a_arr:
        a_dic[c] = a_dic[c] + 1
    for c in b_arr:
        b_dic[c] = b_dic[c] + 1
    for c in a_dic.keys():
        if c in b_dic.keys() and a_dic[c] != b_dic[c]:
            diff = diff + abs(a_dic[c] - b_dic[c])
        if not (c in b_dic.keys()):
            diff = diff + a_dic[c]
    for c in b_dic.keys():
        if not (c in a_dic.keys()):
            diff = diff + b_dic[c]
    return diff


# ----------------- TESTS -----------------

a_1 = "bacdc"
b_1 = "dcbac"
print(making_anagram(a_1, b_1))
# Expected Output: 0

a_2 = "bacdc"
b_2 = "dcbad"
print(making_anagram(a_2, b_2))
# Expected Output: 2
#
a_3 = "cde"
b_3 = "dcf"
print(making_anagram(a_3, b_3))
# Expected Output: 2

a_4 = "cde"
b_4 = "abc"
print(making_anagram(a_4, b_4))
# Expected Output: 4
# Expected Output: 2

a_5 = "abcdefghijk"
b_5 = "almnopqrstu"
print(making_anagram(a_5, b_5))
# Expected Output: 20

a_5 = "a-+][-=jfwinkkkkkk"
b_5 = "ak"
print(making_anagram(a_5, b_5))
# Expected Output: 16
