import sys

"""
Given a 6x6 2D array, A:  a11 a12 a13 a14 a15 a16
                          a21 a22 a23 a24 a25 a26
                          a31 a32 a33 a34 a35 a36
                          a41 a42 a43 a44 a45 a46
                          a51 a52 a53 a54 a55 a56
                          a61 a62 a63 a64 a65 a66
an hourglass in A is a subset of values with indices falling in this pattern in A's graphical representation:a b c
                                                                                                               d
                                                                                                             e f g
There are 16 hourglasses in each 6x6 2D array arr. An hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in the given arr, then print the maximum hourglass sum.
The array will always be 6x6.
"""


def sum_hourglass(arr: list) -> int:
    """
    This function takes as an input a 2D array of integers and returns an integer representing the maximum of
    the hourglass sums.

    Example:
        (1) arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
            sum_hourglass(arr_1) => 7
    """

    max_sum = ~sys.maxsize
    hourglass_sums = []
    for i in range(len(arr) - 2):
        sums = []
        for j in range(len(arr) - 2):
            sums.append(0)
        hourglass_sums.append(sums)

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            temp_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hourglass_sums[i][j] = temp_sum
            if temp_sum > max_sum:
                max_sum = temp_sum
    return f"{max_sum} from {hourglass_sums}"


# ----------------- TESTS -----------------

arr_1 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(sum_hourglass(arr_1))
# Expected Output: 7

arr_2 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
print(sum_hourglass(arr_2))
# Expected Output: 28
#
arr_3 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
print(sum_hourglass(arr_3))
# Expected Output: 19
