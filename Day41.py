# # code chef problem

# Second Largest
# Three numbers A, B and C are the inputs. Write a program to find second largest among them.

# Input Format
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

# Output Format
# For each test case, display the second largest among A, B and C, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ A,B,C ≤ 1000000
# Sample 1:
# Input
# Output
# 3 
# 120 11 400
# 10213 312 10
# 10 3 450
# 120
# 312
# 10

def solve():
    A, B, C = map(int, input().split())
    if (A > B and A < C) or (A < B and A > C):
        print(A)
    elif (B > A and B < C) or (B < A and B > C):
        print(B)
    else:
        print(C)

T = int(input())
for _ in range(T):
    solve()




# ============================================================================================================
    # leetcode problem






# 812. Largest Triangle Area
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
 

# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.














from typing import List
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2
        return max(area(a, b, c) for a, b, c in combinations(points, 3))
