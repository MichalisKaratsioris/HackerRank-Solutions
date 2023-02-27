"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
    - The length of the segment matches Ron's birth month, and,
    - The sum of the integers on the squares is equal to his birthday.
Determine how many ways she can divide the chocolate.
"""


def subarray_division(arr: list, d: int, m: int) -> list:
    """
    This function takes as an input an array of integers and returns an array of arrays of integers.

    Example:
        (1) arr = [2, 2, 1, 3, 2]
            d = 4
            m = 2
            Lily wants to find segments summing to Ron's birthday, d = 4 with a length equaling his birth month, m = 2.
            In this case, there are two segments meeting the criteria: [2, 2] and [1, 3]
    """

    result = []
    n = len(arr)
    for i in range(n - m + 1):
        total = 0
        for j in range(m):
            total = total + arr[i+j]
        if total == d:
            temp = []
            for j in range(m):
                temp.append(arr[i+j])
            result.append(temp)
    return result


# ----------------- TESTS -----------------

arr_1 = [2, 2, 1, 3, 2]
m_1 = 2
d_1 = 4
print(subarray_division(arr_1, d_1, m_1))
# Expected Output: [[2, 2], [1, 3]]

arr_2 = [0, 3, 1, 3, 2, 4, 2, 1, 1]
m_2 = 3
d_2 = 4
print(subarray_division(arr_2, d_2, m_2))
# Expected Output: [[0, 3, 1], [2, 1, 1]]

arr_3 = [10, 0, 9, 1, 9, 4, 6, 1, 8, 3, 7, 4, 9, 1, 10, 1, 5, 5]
m_3 = 2
d_3 = 10
print(subarray_division(arr_3, d_3, m_3))
# Expected Output: [[10, 0], [9, 1], [1, 9], [4, 6], [3, 7], [9, 1], [5, 5]]

arr_4 = [1, 2, 1, 3, 2]
m_4 = 2
d_4 = 3
print(subarray_division(arr_4, d_4, m_4))
# Expected Output: [[1, 2], [2, 1]]

arr_5 = [1, 1, 1, 1, 1, 1]
m_5 = 2
d_5 = 3
print(subarray_division(arr_5, d_5, m_5))
# Expected Output: []

arr_6 = [4]
m_6 = 1
d_6 = 4
print(subarray_division(arr_6, d_6, m_6))
# Expected Output: [[4]]
