# Code Chef Problem



# Finding Shoes
# Chef has 
# N
# N friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his 
# N
# N friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had 
# M
# M left shoes.

# What is the minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his 
# N
# N friends?

# For example, if 
# N
# =
# 2
# N=2, 
# M
# =
# 4
# M=4, then Chef already has 
# 4
# 4 left shoes, so he must buy 
# 2
# 2 extra right shoes to form 
# 2
# 2 pairs of shoes.

# Therefore Chef must buy at least 
# 2
# 2 extra shoes to ensure that he is able to get 
# N
# =
# 2
# N=2 pairs of shoes.

# Input Format
# The first line contains a single integer 
# T
# T - the number of test cases. Then the test cases follow.
# The first line of each test case contains two integers 
# N
# N and 
# M
# M - the number of Chef's friends and the number of left shoes Chef has.
# Output Format
# For each test case, output the minimum number of extra shoes that Chef will have to buy to ensure that he is able to get 
# N
# N pairs of shoes.

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# 0
# ≤
# M
# ≤
# 100
# 0≤M≤100
# Sample 1:
# Input
# Output
# 3
# 2 4
# 6 0
# 4 3
# 2
# 12
# 5
# Explanation:
# Test Case 1: Discussed in the problem statement

# Test Case 2: Chef initially has no left shoes. He must buy 
# 6
# 6 more left shoes and 
# 6
# 6 more right shoes to form 
# 6
# 6 pairs of shoes.

# Test Case 3: Chef initially has 
# 3
# 3 left shoes. He must buy 
# 1
# 1 more left shoe and 
# 4
# 4 more right shoes to form 
# 4
# 4 pairs of shoes.


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    extra_left = max(0, n - m)
    total_extra = n + extra_left
    print(total_extra)
# Test Case 
# 4
# ----------------------------------------------------------------------------
# LEET CODE PROBLEM
        # You are given a 2D 0-indexed integer array dimensions.

        # For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

        # Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

        

        # Example 1:

        # Input: dimensions = [[9,3],[8,6]]
        # Output: 48
        # Explanation: 
        # For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
        # For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
        # So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.
        # Example 2:

        # Input: dimensions = [[3,4],[4,3]]
        # Output: 12
        # Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.
        

        # Constraints:

        # 1 <= dimensions.length <= 100
        # dimensions[i].length == 2
        # 1 <= dimensions[i][0], dimensions[i][1] <= 100

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        
        for l, w in dimensions:
            diag = l*l + w*w   # diagonal squared
            area = l * w
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
        
        return max_area
# Example usage:
# dimensions = [[9,3],[8,6]]