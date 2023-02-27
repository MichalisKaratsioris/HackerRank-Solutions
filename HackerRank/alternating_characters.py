"""
You are given a string containing characters A and B only. Your task is to change it into a string such that
there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
"""


def alternating_characters(s: str) -> int:
    """
    This function takes as an input a string of characters A and B and returns an integer representing the minimum
    number of required deletions of any matching adjacent characters.

    Example:
        (1) s = 'AABAAB'
            s' = 'ABAB'
            number of deletions : 2
            alternating_characters(s) => 2
    """

    num_of_deletions = 0
    s_arr = []
    for i in range(len(s)):
        s_arr.append(s[i])
    for i in range(len(s_arr) - 1):
        if s_arr[i] == s_arr[i + 1]:
            num_of_deletions = num_of_deletions + 1
    return num_of_deletions


# ----------------- TESTS -----------------

s_1 = "AABAAB"
print(alternating_characters(s_1))
# Expected Output: 2

s_2 = "AAAA"
print(alternating_characters(s_2))
# Expected Output: 3

s_3 = "BBBBB"
print(alternating_characters(s_3))
# Expected Output: 4

s_4 = "ABABABAB"
print(alternating_characters(s_4))
# Expected Output: 0

s_5 = "BABABA"
print(alternating_characters(s_5))
# Expected Output: 0

s_6 = "AAABBB"
print(alternating_characters(s_6))
# Expected Output: 4
