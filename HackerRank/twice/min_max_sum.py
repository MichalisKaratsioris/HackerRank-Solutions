"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly 
four of the five integers. Then print the respective minimum and maximum values as a single line of two 
space-separated long integers.

Example: arr[1, 3, 5, 7, 9]
The minimum sum is 16 and the maximum sum is 24. The function prints

                16 24

Function Description: Complete the miniMaxSum function in the editor below, which has the following parameter(s):

                arr: an array of  integers

Print: Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Input Format: A single line of five space-separated integers.

Constraints:

    1 <= arr[i] <= 10**(9)

Output Format: Print two space-separated long integers denoting the respective minimum and maximum values that can 
be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input: arr = [1, 2, 3, 4, 5]

Sample Output: 10 14

Hints: Beware of integer overflow! Use 64-bit Integer.
"""

def miniMaxSum(nums: list) -> str:
    nums.sort()
    minimum = sum(nums[:-1])
    maximum = sum(nums[1:])
    return f"{minimum} {maximum}"

arr = [1, 2, 3, 4, 5]
print(miniMaxSum(arr))
# Output: 10 14

arr = [1, 3, 5, 7, 9]
print(miniMaxSum(arr))
# Output: 16 24

