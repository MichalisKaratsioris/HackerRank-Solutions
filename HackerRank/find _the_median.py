"""
mock test
"""

def findMedian(nums: list) -> int:
    nums.sort()
    return nums[len(nums)//2]

arr = [5, 3, 1, 2, 4]
print(findMedian(arr))
# Output: 3

arr = [0, 1, 2, 4, 6, 5, 3]
print(findMedian(arr))
# Output: 3
