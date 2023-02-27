"""
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of
their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
"""


def birthday_cake_candles(arr: list) -> int:
    """
    This function takes as an input an array of integers and returns an integer representing the frequency of the
    greatest number inside the provided array.

    Example:
        (1) arr = [4, 4, 1, 3]
            birthday_cake_candles(arr) => 2
    """

    f = 0
    greatest = max(arr)
    for number in arr:
        if number == greatest:
            f = f + 1
    return f


# ----------------- TESTS -----------------

arr_1 = [4, 4, 1, 3]
print(birthday_cake_candles(arr_1))
# Expected Output: 2

arr_2 = [3, 2, 1, 3]
print(birthday_cake_candles(arr_2))
# Expected Output: 2

arr_3 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]
print(birthday_cake_candles(arr_3))
# Expected Output: 4
