"""
mock test: Given a 2n x 2n matrix, make sure that the n x n matrix on the top-left corner has the maximum sum possible.

Example:

arr = [[1, 2], [3, 4]] => 2x2 => n = 1
result = [[4, 2], [1, 3]]
"""

def flippingMatrix(matrix: list) -> int:
    # n = len(arr) // 2
    # for i in range(n):
    #     for j in range(n):
    #         # scenarios comparing the corners between them and choosing the greatest amongst them to bring in the left-top corner.
    #         # this brings the [0][n] in [0][0]
    #         if arr[i][j] < arr[i][-1-j]:
    #             arr[i][j], arr[i][-1-j] = arr[i][-1-j], arr[i][j]

    #         # this brings the [n][n] in [0][0]
    #         if arr[i][j] < arr[-1-j][-1-j]:
    #             arr[i][j], arr[-1-j][-1-j] = arr[-1-j][-1-j], arr[i][j]

    #         # this brings the [n][0] in [0][0]
    #         if arr[i][j] < arr[-1-j][i]:
    #             arr[i][j], arr[-1-j][i] = arr[-1-j][i], arr[i][j]

    #         # Now, I have to do the same for all rest elements of the nxn matrix...
    # return arr

arr = [[1, 2], [3, 4]]
print(flippingMatrix(arr))
# Output: [[4, 2], [1, 3]] => 4

arr = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(arr))
# Output: [[119, 114, 42, 112], [56, 125, 101, 49], [15, 78, 56, 43], [62, 98, 83, 108]] => 414
