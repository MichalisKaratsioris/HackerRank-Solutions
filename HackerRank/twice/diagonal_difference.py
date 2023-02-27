"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""


def diagonal_difference(arr: list) -> int:
    """
     This function takes as an input an n-matrix with integer elements arr, and returns the difference of the sum
     of its diagonals.

     Example:
         (1) arr =  [1, 2, 3]
                    [4, 5, 6]
                    [7, 8, 9]
            diagonal_difference(arr) => |(1 + 5 + 9) - (3 + 5 + 7)| = 0
         (2) arr =  [1, 2, 3]
                    [4, 5, 6]
                    [9, 8, 9]
            diagonal_difference(arr) => |(1 + 5 + 9) - (3 + 5 + 9)| = 2
    """
    left_right_diagonal_sum = 0
    right_left_diagonal_sum = 0
    for i in range(len(arr)):
        left_right_diagonal_sum = left_right_diagonal_sum + arr[i][i]
        right_left_diagonal_sum = right_left_diagonal_sum + arr[i][-1 - i]
    return abs(left_right_diagonal_sum - right_left_diagonal_sum)


# ----------------- TESTS -----------------

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_difference(arr1)
# Expected Output: 0

arr2 = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
diagonal_difference(arr2)
# Expected Output: 2

arr1 = [[1, 2, 1], [4, 5, 6], [9, 8, 9]]
diagonal_difference(arr1)
# Expected Output: 0

arr1 = [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_difference(arr1)
# Expected Output: 9
