# #  CODE CHEF PROBLEM
# Mario and Transformation
# Mario transforms each time he eats a mushroom as follows:

# If he is currently small, he turns normal.
# If he is currently normal, he turns huge.
# If he is currently huge, he turns small.
# Given that Mario was initially normal, find his size after eating 
# X
# X mushrooms.

# Input Format
# The first line of input will contain one integer 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, containing one integer 
# X
# X.
# Output Format
# For each test case, output in a single line Mario's size after eating 
# X
# X mushrooms.

# Print:

# NORMAL
# NORMAL, if his final size is normal.
# HUGE
# HUGE, if his final size is huge.
# SMALL
# SMALL, if his final size is small.
# You may print each character of the answer in either uppercase or lowercase (for example, the strings 
# Huge
# Huge, 
# hUgE
# hUgE, 
# huge
# huge and 
# HUGE
# HUGE will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# X
# ≤
# 100
# 1≤X≤100
# Sample 1:
# Input
# Output
# 3
# 2
# 4
# 12
# SMALL
# HUGE
# NORMAL
# Explanation:
# Test case 
# 1
# 1: Mario's initial size is normal. On eating the first mushroom, he turns huge. On eating the second mushroom, he turns small.

# Test case 
# 2
# 2: Mario's initial size is normal. On eating the first mushroom, he turns huge. On eating the second mushroom, he turns small. On eating the third mushroom, he turns normal. On eating the fourth mushroom, he turns huge.


def solve():
    x = int(input())
    x %= 3
    if x == 0:
        print("NORMAL")
    elif x == 1:
        print("HUGE")
    else:
        print("SMALL")

t = int(input())
for _ in range(t):
    solve()


    # --------------------------------------------------------
# 2nd Question
# 3446. Sort Matrix by Diagonals
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an n x n square matrix of integers grid. Return the matrix such that:

# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.
 

# Example 1:

# Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

# Output: [[8,2,3],[9,6,7],[4,5,1]]

# Explanation:



# The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

# [1, 8, 6] becomes [8, 6, 1].
# [9, 5] and [4] remain unchanged.
# The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

# [7, 2] becomes [2, 7].
# [3] remains unchanged.
# Example 2:

# Input: grid = [[0,1],[1,2]]

# Output: [[2,1],[1,0]]

# Explanation:



# The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

# Example 3:

# Input: grid = [[1]]

# Output: [[1]]

# Explanation:

# Diagonals with exactly one element are already in order, so no changes are needed.

 

# Constraints:

# grid.length == grid[i].length == n
# 1 <= n <= 10
# -105 <= grid[i][j] <= 105

from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Collect all diagonals
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: Sort diagonals based on their position
        for key in diagonals:
            if key >= 0:  # bottom-left (i >= j)
                diagonals[key].sort(reverse=True)  # non-increasing
            else:  # top-right (i < j)
                diagonals[key].sort()  # non-decreasing

        # Step 3: Refill the grid
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid

# Example usage:
# grid = [[1,7,3],[9,8,2],[4,5,6]]
# Output: [[8,2,3],[9,6,7],[4,5,1]]

# --------------------------------------------------------
# 3rd Question  