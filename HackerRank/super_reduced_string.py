"""
Reduce a string of lowercase characters in range ascii[a-z] by doing a series of operations. In each operation, select
a pair of adjacent letters that match, and delete them. Delete as many characters as possible using this method and
return the resulting string. If the final string is empty, return "Empty String".
"""


def super_reduced_string(s: str) -> str:
    """
    This function takes as an input a string (s) and returns a string deleting all duplicate characters.

    Example:
        (1) s = 'aab'
            super_reduced_string(s) => 'b'
    """

    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    while True:
        change = 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr.remove(arr[i + 1])
                arr.remove(arr[i])
                change = 0
                break
        if change == 1:
            break
    if len(arr) != 0:
        reduced_string = ''
        for character in arr:
            reduced_string = reduced_string + f"{character}"
        return reduced_string
    return "Empty String"

    # Solution #2
    # buff = []
    # for item in s:
    #     if buff and item == buff[-1]:
    #         buff.pop()
    #     else:
    #         buff.append(item)
    # if len(buff) != 0:
    #     return ''.join(buff)
    # return "Empty String"


# ----------------- TESTS -----------------

s_1 = "aab"
print(super_reduced_string(s_1))
# Expected Output: b

s_2 = "abba"
print(super_reduced_string(s_2))
# Expected Output: Empty String
#
s_3 = "aaabccddd"
print(super_reduced_string(s_3))
# Expected Output: abd

s_4 = "aa"
print(super_reduced_string(s_4))
# Expected Output: Empty String

s_5 = "baab"
print(super_reduced_string(s_5))
# Expected Output: Empty String
