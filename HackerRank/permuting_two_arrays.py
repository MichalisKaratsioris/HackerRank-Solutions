"""
There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation
A'[i] + B'[i] >= k holds for all i, where 0<= i < n. There will be q queries consisting of A, B, and k.
For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.
"""


def array_permutation(arr1: list, arr2: list, k: int) -> str:
    """
    This function takes as an input two arrays with n integers each and after permuting them, it checks q times,
    if the following relation holds: A'[i] + B'[i] >= k holds for all i, where 0<= i < n. If it holds, then return YES,
    otherwise return NO.

    Example:
        (1) A = [0, 1], B = [0, 2] and k = 1
            A valid A', B' would be: A' = [1, 0], B' = [0, 2] because: 1 + 0 >= 1 and 0 + 2 >= 1. Returns YES.

    """

    n = len(arr1)
    sum_a = sum(arr1)
    sum_b = sum(arr2)
    if (sum_b + sum_a) >= (n * k):
        return "YES"
    return "NO"


# ----------------- TESTS -----------------

arr_1 = [0, 1]
arr_2 = [0, 2]
k_1 = 1
print(array_permutation(arr_1, arr_2, k_1))
# Expected Output: YES

arr_3 = [2, 1, 3]
arr_4 = [7, 9, 8]
k_2 = 10
print(array_permutation(arr_3, arr_4, k_2))
# Expected Output: YES

arr_5 = [1, 2, 2, 1]
arr_6 = [3, 3, 3, 4]
k_3 = 5
print(array_permutation(arr_5, arr_6, k_3))
# Expected Output: NO
