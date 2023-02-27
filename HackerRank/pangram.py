"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram
in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
"""


def pangram(s: str) -> str:
    """
    This function takes as an input a string and checks if the string contains at least once every letter of
    the English alphabet.

    Example:
        (1) s = 'The quick brown fox jumps over the lazy dog'
            pangram(s) => pangram.

        (2) s = 'We promptly judged antique ivory buckles for the prize'
            pangram(s) => not pangram.
    """

    arr = s.split()
    l_str = ''
    for word in arr:
        l_str = l_str + word.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    freq = []
    for _ in range(len(letters)):
        freq.append(0)

    # counting each letter and storing its frequency
    for i in range(len(l_str)):
        for j in range(len(letters)):
            if l_str[i] == letters[j]:
                freq[j] = freq[j] + 1
    total_sum = 0
    count_zeros = 0
    for f in freq:
        total_sum = total_sum + f
        if f == 0:
            count_zeros = count_zeros + 1
    if count_zeros == 0:
        return "pangram"
    return "not pangram"


# ----------------- TESTS -----------------

s_1 = 'The quick brown fox jumps over the lazy dog'
print(s_1, ": ", pangram(s_1))
# Expected Output: pangram

s_2 = 'We promptly judged antique ivory buckles for the prize'
print(s_2, ": ", pangram(s_2))
# Expected Output: not pangram

s_3 = 'abcdefghijklmnopqrstuvwxyz'
print(s_3, ": ", pangram(s_3))
# Expected Output: pangram
