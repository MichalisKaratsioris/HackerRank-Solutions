"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
each sock, determine how many pairs of socks with matching colors there are.
"""


def sales_by_match(arr: list) -> int:
    """
    This function takes as an input an array of integers and returns an integer which represents the total number
    of matching integers.

    Example:
        (1) arr = [1, 2, 1, 2, 1, 3, 2]
            sales_by_match(arr) => 2
    """

    # initiating the frequency list
    freq = []
    s = set(arr)
    for _ in range(len(s)):
        freq.append(0)
    index = 0
    for n in s:
        count = 0
        for m in arr:
            if n == m:
                count = count + 1
        freq[index] = freq[index] + count
        index = index + 1
    pairs = 0
    for f in freq:
        if f > 1:
            pairs = pairs + f//2
    return pairs


# ----------------- TESTS -----------------

arr_1 = [1, 2, 1, 2, 1, 3, 2]
print(sales_by_match(arr_1))
# Expected Output: 2

arr_2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sales_by_match(arr_2))
# Expected Output: 3

arr_3 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
print(sales_by_match(arr_3))
# Expected Output: 6
