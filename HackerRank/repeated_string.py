"""
There is a string, s, of lowercase English letters that is repeated infinitely many times.
Given an integer, n, find and print the number of letter a in the first n letters of the infinite string.
"""


def repeated_string(s: str, n: int) -> int:
    """
    This function takes as an input a string s and an integer n, and returns an integer representing the frequency of
    the letter a inside the substring of length n. The substring is supposedly taken from the infinite repetition of s.

    Example:
        (1) s = 'abcac'
            n = 10
            repeated_string(s, n) => 4
    """

    f = 0
    s = s.lower()
    while len(s) < n:
        s = s + s
    sub = s[0:n]
    for letter in sub:
        if letter == 'a':
            f = f + 1
    return f


# ----------------- TESTS -----------------

s_1 = 'abcac'
n_1 = 10
print(repeated_string(s_1, n_1))
# Expected Output: 4

s_2 = 'abcaca'
n_2 = 20
print(repeated_string(s_2, n_2))
# Expected Output: 10

s_3 = 'abcdeaghia'
n_3 = 100
print(repeated_string(s_3, n_3))
# Expected Output: 30
