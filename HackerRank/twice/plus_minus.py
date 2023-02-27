"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to 10**(-4) are acceptable.
"""


def plus_minus(arr: list, precision: int) -> list:
    """
    This function takes as an input an array of integers arr and an integer precision, and returns a float for
    the percentages of positive, negative and zeros inside the array, with a given precision in decimal digits.

    Examples:
        (1) arr_1 = [-4, 3, -9, 0, 4, 1]
            precision_1 = 2
            plus_minus(arr_1, precision_1) =>   [0.50, 0.33, 0.17]

        (2) arr_2 = [1, 2, 3, -1, -2, -3, 0, 0]
            precision_2 = 6
            plus_minus(arr_2, precision_2) =>   [0.375000, 0.375000, 0.250000]
    """

    count_p = 0
    count_n = 0
    count_z = 0
    for number in arr:
        if number > 0:
            count_p = count_p + 1
        elif number < 0:
            count_n = count_n + 1
        else:
            count_z = count_z + 1
    return [f"{round(count_p / len(arr), 6):.{precision}f}", f"{round(count_n / len(arr), 6):.{precision}f}", f"{round(count_z / len(arr), 6):.{precision}f}"]


# ----------------- TESTS -----------------

print(plus_minus([-4, 3, -9, 0, 4, 1], 2))
# Expected Output: ['0.50', '0.33', '0.17']

print(plus_minus([1, 2, 3, -1, -2, -3, 0, 0], 6))
# Expected Output: ['0.375000', '0.375000', '0.250000']