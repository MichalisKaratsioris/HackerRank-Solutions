"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Example: grid = ['abc', 'ade', 'efg']. The grid is illustrated below.

        a b c
        a d e
        e f g

The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer 
would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

Function Description: Complete the gridChallenge function in the editor below, which has the following parameter(s):

        string grid[n]: an array of strings
    Returns:
        string: either YES or NO

        
Constraints: Each string consists of lowercase letters in the range ascii[a-z]

Output Format: For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically 
ascending in both its rows and columns, or NO otherwise.

Sample Input: grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

        e   b   a   c   d   
        f   g   h   i   j
        o   l   m   k   n
        t   r   p   q   s
        x   y   w   u   v

Sample Output: YES

Explanation: The x grid in the  test case can be reordered to

        a   b   c   d   e
        f   g   h   i   j
        k   l   m   n   o
        p   q   r   s   t
        u   v   w   x   y

This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.
"""

def gridChallenge(grid: list) -> str:
    for s in grid:
        if len(s) != len(grid[0]):
            return "NO"
    result = []
    for s in grid:
        temp = list(s)
        temp.sort()
        result.append("".join(temp))
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if result[i][j] > result[i + 1][j]:
                return "NO"
    return "YES"
    
        

arr = ['abc', 'ade', 'efg']
print(gridChallenge(arr))
# Output: YES

arr = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(arr))
# Output: YES

arr = ['ebacd', 'fghi', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(arr))
# Output: NO

arr = ['abc', 'lmp', 'qrt']
print(gridChallenge(arr))
# Output: YES

arr = ['mpxz', 'abcd', 'wlmf']
print(gridChallenge(arr))
# Output: NO

arr = ['abc', 'hjk', 'mpq', 'rtv']
print(gridChallenge(arr))
# Output: YES