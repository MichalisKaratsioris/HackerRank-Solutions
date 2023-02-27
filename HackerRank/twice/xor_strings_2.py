"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.
Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
To know more about XOR: https://en.wikipedia.org/wiki/Exclusive_or
Debug the given function strings_xor:

                def strings_xor(s, t):
                    res = ""
                    for i in range(len(s)):
                        if s[i] = t[i]:
                            res = '0';
                        else:
                            res = '1';

                    return res

                s = input()
                t = input()
                print(strings_xor(s, t))

to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code, and you cannot add or remove lines to the code.
"""


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        # first correction was "==" instead of "="
        if s[i] == t[i]:
            # second correction was to delete ";" and add "res + " before "0"
            res = res + '0'
        else:
            # third correction was to delete ";" and add "res + " before "1"
            res = res + '1'

    return res


# ----------------- TESTS -----------------

s_1 = input()
# 10101, 1111111111, 0000000000, 0000, 1111
t_1 = input()
# 00101, 0000000000, 1111111111, 0000, 1111
print(strings_xor(s_1, t_1))
# Expected Output: 10000, 1111111111, 1111111111, 0000, 0000
