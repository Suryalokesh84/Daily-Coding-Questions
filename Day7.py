# # ✅ Question:

# A player in discus throw is given 3 throws, and the throw with the longest distance is regarded as their final score.

# You are given the distances for all 3 throws of a player. Determine the final score of the player.

# Input Format:

# The first line will contain an integer T (number of test cases).

# Each test case contains 3 integers A, B, C — the distances in each throw.

# Output Format:

# For each test case, print the final score of the player.

# Constraints:

# 1 ≤ T ≤ 100

# 1 ≤ A, B, C ≤ 100

# Sample Input:
# 3
# 10 15 8
# 32 32 32
# 82 45 54

# Sample Output:
# 15
# 32
# 82

# Number of test cases
T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    # Final score is the maximum distance
    print(max(A, B, C))



# ✅ Question:

# You are given an m x n binary matrix mat.
# Return the number of submatrices that contain only ones.

# Input Format:

# A 2D list mat of size m x n, where each element is either 0 or 1.

# Output Format:

# An integer representing the total number of submatrices that consist of only 1s.

# Constraints:

# 1 ≤ m, n ≤ 150

# mat[i][j] is either 0 or 1

# Example 1:
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13

# Example 2:
# Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# Output: 24

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        result = 0
        for i in range(m):
            for j in range(n):
                if heights[i][j] > 0:
                    h = heights[i][j]
                    for k in range(j, -1, -1):
                        if heights[i][k] == 0:
                            break
                        h = min(h, heights[i][k])
                        result += h
        return result
# Example usage:
# mat = [[1,0,1],[1,1,0],[1,1,0]]