"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""


def lonely_integer(arr):
    """
    This function takes as an input an array of integers arr and returns the integer that appears only once
    inside the provided array.

    Example:
        (1) arr1 = [1, 2, 3, 4, 3, 2, 1]
            lonely_integer(arr1) => 4
        (2) arr2 = [1, 2, 1, 1, 1, 1, 2, 10]
            lonely_integer(arr2) => 10
    """
    counts = []
    for number1 in arr:
        count = 0
        for number2 in arr:
            if number2 == number1:
                count = count + 1
        counts.append(count)
    for i in range(len(counts)):
        if counts[i] == 1:
            return arr[i]


# ----------------- TESTS -----------------

arr1 = [1, 2, 3, 4, 3, 2, 1]
print(lonely_integer(arr1))
# Expected Output: 4

arr2 = [1, 2, 1, 1, 1, 1, 1]
print(lonely_integer(arr2))
# Expected Output: 2

arr3 = [1, 2, 1, 1, 1, 1, 2]
print(lonely_integer(arr3))
# Expected Output: (nothing...)

arr4 = [1, 2, 3, 2, 1]
print(lonely_integer(arr4))
# Expected Output: 3

arr5 = [1, 2, 1, 1, 1, 1, 1, 4, 5, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 2, 0]
print(lonely_integer(arr5))
# Expected Output: 0

arr6 = [1, 2, 1, 1, 1, 1, 2, 10]
print(lonely_integer(arr6))
# Expected Output: 10
