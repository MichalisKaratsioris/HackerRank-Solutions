"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files. Given an
array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence
will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last k elements
are in decreasing order, where k=(n+1)/2. You need to find, lexicographically, the smallest zigzag sequence of the given
array.
"""


def zig_zag_sequence(arr: list, n: int) -> list:

    arr.sort()
    mid = int((n + 1)/2)
    arr[mid], arr[n-1] = arr[n-1], arr[mid]

    st = mid + 1
    ed = n - 1
    while st <= ed:
        arr[st], arr[ed] = arr[ed], arr[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(arr[i])
        else:
            print(arr[i], end=' ')
    return


# ----------------- TESTS -----------------

arr_1 = [2, 3, 5, 1, 4]
n_1 = 3
zig_zag_sequence(arr_1, n_1)
# Expected Output: [1, 4, 5, 3, 2]
