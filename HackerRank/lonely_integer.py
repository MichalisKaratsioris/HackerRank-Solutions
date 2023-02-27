"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example: arr = [1, 2, 3, 4, 3, 2, 1]. The unique element is 4.

Function Description: Complete the lonelyinteger function in the editor below, which has the following parameter(s):
        int a[n]: an array of integers
    Returns:
        int: the element that occurs only once
"""

def lonelyInteger(nums: list) -> int:
    elements = {}
    for i, num in enumerate(nums):
        if num in elements:
            elements[num] += 1
        else:
            elements[num] = 1
    for key in elements.keys():
        if elements[key] == 1:
            return key

arr = [1, 2, 3, 4, 3, 2, 1]
print(lonelyInteger(arr))
# Output: 4

arr = [1]
print(lonelyInteger(arr))
# Output: 1

arr = [1, 1, 2]
print(lonelyInteger(arr))
# Output: 2

arr = [0, 0, 1, 2, 1]
print(lonelyInteger(arr))
# Output: 2


