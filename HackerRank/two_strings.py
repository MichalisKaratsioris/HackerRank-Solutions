"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.
"""


def two_strings(s: str, t: str) -> str:
    """
    This function takes as an input two strings, s and t, and returns a string, "Yes" or "No", depending if s and t
    share a common substring.

    Example:
        (1) s = "and"
            t = "art"
            two_strings(s, t) => "Yes"
    """

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                return "Yes"
    return "No"


# ----------------- TESTS -----------------

s_1 = 'and'
t_1 = 'art'
print(two_strings(s_1, t_1))
# Expected Output: Yes

s_2 = 'be'
t_2 = 'cat'
print(two_strings(s_2, t_2))
# Expected Output: No

s_3 = 'hello'
t_3 = 'world'
print(two_strings(s_3, t_3))
# Expected Output: Yes

s_4 = 'hi'
t_4 = 'world'
print(two_strings(s_4, t_4))
# Expected Output: No
