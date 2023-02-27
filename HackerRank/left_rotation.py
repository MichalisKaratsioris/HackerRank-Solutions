"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left
rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2]. Note that the lowest
index item moves to the highest index in a rotation. This is called a circular array.

Given an array arr of n integers and a number, d, perform d left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.
"""


def left_rotation(arr: list, d: int) -> list:
    """
    This function takes as an input an array of integers and an integer, and return an integer representing
    the number of left-rotations the function applies to the provided array.

    Example:
        (1) arr = [1, 2, 3, 4, 5]
            d = 2
            left_rotation(arr, d) => 3 4 5 1 2
    """

    for i in range(d):
        d = arr[0]
        arr.append(d)
        arr.remove(d)
    arr_str = ''
    for number in arr:
        arr_str = f"{arr_str} {number}"
    return arr_str


# ----------------- TESTS -----------------

arr_1 = [1, 2, 3, 4, 5]
d_1 = 2
print(left_rotation(arr_1, d_1))
# Expected Output: 3 4 5 1 2

arr_2 = [1, 2, 3, 4, 5]
d_2 = 1
print(left_rotation(arr_2, d_2))
# Expected Output: 2 3 4 5 1

arr_3 = [1, 2, 3, 4, 5]
d_3 = 4
print(left_rotation(arr_3, d_3))
# Expected Output: 5 1 2 3 4

arr_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d_4 = 5
print(left_rotation(arr_4, d_4))
# Expected Output: 6 7 8 9 1 2 3 4 5
