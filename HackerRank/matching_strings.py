"""
There is a collection of input_strings (s_1) and a collection of query_strings (s_2).
For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.
"""


def matching_strings(s_1: list, s_2: list) -> list:
    """
    This function takes as an input two arrays of strings, s1 and s2, and counts how many times each string from the
    second array occurs in the first. It returns an array of integers with the counts.

    Example:
    -   s_1 = ['ab', 'ab', 'abc']
        s_2 = ['ab', 'abc', 'bc']
        matching_strings(s_1, s_2) => [2, 1, 0]
    """
    counts = []
    for i in range(len(s_2)):
        count = 0
        for sj in s_1:
            if s_2[i].__eq__(sj):
                count = count + 1
        counts.append(count)
    return counts


# ----------------- TESTS -----------------

s1 = ['ab', 'ab', 'abc']
s2 = ['ab', 'abc', 'bc']
print(matching_strings(s1, s2))
# Expected Output: [2, 1, 0]

s1 = ['aba', 'baba', 'aba', 'xzxb']
s2 = ['aba', 'xzxb', 'ab']
print(matching_strings(s1, s2))
# Expected Output: [2, 1, 0]

s1 = ['def', 'de', 'fgh']
s2 = ['de', 'lmn', 'fgh']
print(matching_strings(s1, s2))
# Expected Output: [1, 0, 1]

s1 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
s2 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
print(matching_strings(s1, s2))
# Expected Output: [1, 3, 4, 3, 2]
