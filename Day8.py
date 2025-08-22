# Problem: Reverse a String

# Write a Python function that takes a string as input and returns the string reversed.

# Example:

# Input: "hello"

# Output: "olleh"

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# Problem: Reverse a String


from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        min_row, max_row = m, -1
        min_col, max_col = n, -1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)
#3195 leet code