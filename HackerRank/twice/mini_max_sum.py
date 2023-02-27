"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing
exactly four of the five integers. Then print the respective minimum and maximum values as a single line
of two space-separated long integers.

Example: arr = [1, 3, 5, 7, 9]
The minimum sum is 16 and the maximum sum is 24. The function prints: 16 24
"""


def min_max_sum(arr: list) -> str:
    """
    This function takes as an input an array of integers arr and returns the minimum and maximum sums separated
    by space.
        - Minimum sum is the sum of all the integers except the greatest one.
        - Maximum sum is the sum of all the integers except the smallest one.

    Examples:
        (1) arr_1 = [1, 2, 3, 4, 5]
            min_max_sum(arr_1) => 10 14
        (2) arr_2 = [7, 69, 2, 221, 8974]
            min_max_sum(arr_2) => 299 9271
    """
    arr.sort()
    total = 0
    for number in arr:
        total = total + number
    min_sum = total - arr[-1]
    max_sum = total - arr[0]
    return f"{min_sum} {max_sum}"


# ----------------- TESTS -----------------

print(min_max_sum([1, 2, 3, 4, 5]))
# Expected Output: 10 14


print(min_max_sum([7, 69, 2, 221, 8974]))
# Expected Output: 299 9271
