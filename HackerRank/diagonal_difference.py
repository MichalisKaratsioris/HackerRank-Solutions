"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals. For example, 
the square matrix arr is shown below:

    1 2 3
    4 5 6
    9 8 9  

The left-to-right diagonal gives 15. The right to left diagonal gives 17. Their absolute difference is |15 - 17| = 2.

Function description: Complete the diagonalDifference function in the editor below, which takes the following parameter:

        int arr[n][m]: an array of integers
    Return:
        int: the absolute diagonal difference

Constraints:

        -100 <= arr[i] <= 100

Output Format: Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input: arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

Sample Output: 15
"""

def diagonalDifference(nums: list) -> int:
    n = len(nums)
    l2r_diagonal = 0
    r2l_diagonal = 0
    for i in range(n):
        l2r_diagonal += nums[i][i]
        r2l_diagonal += nums[i][-i - 1]
    return abs(l2r_diagonal - r2l_diagonal)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))
# Output: 15

arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
print(diagonalDifference(arr))
# Output: 2
