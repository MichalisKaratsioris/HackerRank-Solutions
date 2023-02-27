"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though 
answers with absolute error of up to  are acceptable.

Example: arr = [1, 1, 0, -1, -1]
There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5=0.400000, 2/5=0.400000 
and 1/5=0.200000. Results are printed as:

            0.400000
            0.400000
            0.200000

Function Description: Complete the plusMinus function in the editor below, which has the following parameter(s):

            int arr[n]: an array of integers

Print: Print the ratios of positive, negative and zero values in the array. Each value should be printed on a 
separate line with  digits after the decimal. The function should not return a value.

Input Format: The first line contains an integer, , the size of the array. The second line contains  space-separated 
integers that describe .

Constraints:

            0 < n <= 100
            -100 <= arr[i] <= 100

Output Format: Print the following  lines, each to  decimals:
    
    1. proportion of positive values
    2. proportion of negative values
    3. proportion of zeros

Sample Input: arr = [-4, 3, -9, 0, 4, 1]

Sample Output:

            0.500000
            0.333333
            0.166667

Explanation: There are 3 positive numbers, 2 negative numbers, and 1 zero in the array. The proportions of occurrence 
are positive: 3/6, negative: 2/6 and zeros: 1/6.
"""

def plusMinus(nums: list) -> str:
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        elif num > 0:
            positive_count += 1
        else:
            negative_count += 1
    p_ratio = positive_count/len(nums)
    n_ratio = negative_count/len(nums)
    z_ratio = zero_count/len(nums)
    return f"{p_ratio:06f}\n{n_ratio:06f}\n{z_ratio:06f}"

arr = [1, 1, 0, -1, -1]
print(plusMinus(arr))
"""
Output:
    0.400000
    0.400000
    0.200000
"""

arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))
"""
Output:
    0.500000
    0.333333
    0.166667
"""

arr = [1, 2, 3, -1, -2, -3, 0, 0]
print(plusMinus(arr))
"""
Output:
    0.375000
    0.375000
    0.250000
"""

