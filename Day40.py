# # code chef problem

# A or B
# There are two problems in a contest.

# Problem A is worth 
# 500
# 500 points at the start of the contest.
# Problem B is worth 
# 1000
# 1000 points at the start of the contest.
# Once the contest starts, after each minute:

# Maximum points of Problem A reduce by 
# 2
# 2 points .
# Maximum points of Problem B reduce by 
# 4
# 4 points.
# It is known that Chef requires 
# X
# X minutes to solve Problem A correctly and 
# Y
# Y minutes to solve Problem B correctly.

# Find the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers 
# X
# X and 
# Y
# Y - the time required to solve problems 
# A
# A and 
# B
# B in minutes respectively.
# Output Format
# For each test case, output in a single line, the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# X
# ,
# Y
# ≤
# 100
# 1≤X,Y≤100
# Sample 1:
# Input
# Output
# 4
# 10 20
# 8 40
# 15 15
# 20 10
# 1360
# 1292
# 1380
# 1400
# Explanation:
# Test Case 
# 1
# 1: If Chef attempts in the order 
# A
# →
# B
# A→B then he submits Problem A after 
# 10
# 10 minutes and Problem B after 
# 30
# 30 minutes.
# Thus, he gets 
# 500
# −
# 10
# ⋅
# 2
# =
# 480
# 500−10⋅2=480 points for problem A and 
# 1000
# −
# 30
# ⋅
# 4
# =
# 880
# 1000−30⋅4=880 points for problem B. Thus, total 
# 480
# +
# 880
# =
# 1360
# 480+880=1360 points for both the problems.

# If Chef attempts in the order 
# B
# →
# A
# B→A then he submits Problem B after 
# 20
# 20 minutes and Problem A after 
# 30
# 30 minutes.
# Thus, he gets 
# 1000
# −
# 20
# ⋅
# 4
# =
# 920
# 1000−20⋅4=920 points for Problem B and 
# 500
# −
# 30
# ⋅
# 2
# =
# 440
# 500−30⋅2=440 points for Problem A. Thus total 
# 920
# +
# 440
# =
# 1360
# 920+440=1360 points for both the problems.

# So, in both cases Chef gets 
# 1360
# 1360 points in total.

# Test Case 
# 2
# 2: If Chef attempts in the order 
# A
# →
# B
# A→B then he submits Problem A after 
# 8
# 8 minutes and Problem B after 
# 48
# 48 minutes.
# Thus, he gets 
# 500
# −
# 8
# ⋅
# 2
# =
# 484
# 500−8⋅2=484 points for problem A and 
# 1000
# −
# 48
# ⋅
# 4
# =
# 808
# 1000−48⋅4=808 points for problem B. Thus, total 
# 484
# +
# 808
# =
# 1292
# 484+808=1292 points for both the problems.

# If Chef attempts in the order 
# B
# →
# A
# B→A then he submits Problem B after 
# 40
# 40 minutes and Problem A after 
# 48
# 48 minutes.
# Thus, he gets 
# 1000
# −
# 40
# ⋅
# 4
# =
# 840
# 1000−40⋅4=840 points for Problem B and 
# 500
# −
# 48
# ⋅
# 2
# =
# 404
# 500−48⋅2=404 points for Problem A. Thus total 
# 840
# +
# 404
# =
# 1244
# 840+404=1244 points for both the problems.

# So, Chef will attempt in the order 
# A
# →
# B
# A→B and thus obtain 
# 1292
# 1292 points.

# Test Case 
# 3
# 3: If Chef attempts in the order 
# A
# →
# B
# A→B then he submits Problem A after 
# 15
# 15 minutes and Problem B after 
# 30
# 30 minutes.
# Thus, he gets 
# 500
# −
# 15
# ⋅
# 2
# =
# 470
# 500−15⋅2=470 points for problem A and 
# 1000
# −
# 30
# ⋅
# 4
# =
# 880
# 1000−30⋅4=880 points for problem B. Thus, total 
# 470
# +
# 880
# =
# 1350
# 470+880=1350 points for both the problems.

# If Chef attempts in the order 
# B
# →
# A
# B→A then he submits Problem B after 
# 15
# 15 minutes and Problem A after 
# 30
# 30 minutes.
# Thus, he gets 
# 1000
# −
# 15
# ⋅
# 4
# =
# 940
# 1000−15⋅4=940 points for Problem B and 
# 500
# −
# 30
# ⋅
# 2
# =
# 440
# 500−30⋅2=440 points for Problem A. Thus total 
# 940
# +
# 440
# =
# 1380
# 940+440=1380 points for both the problems.

# So, Chef will attempt in the order 
# B
# →
# A
# B→A and thus obtain 
# 1380
# 1380 points.

# Test Case 
# 4
# 4: If Chef attempts in the order 
# A
# →
# B
# A→B then he submits Problem A after 
# 20
# 20 minutes and Problem B after 
# 30
# 30 minutes.
# Thus, he gets 
# 500
# −
# 20
# ⋅
# 2
# =
# 460
# 500−20⋅2=460 points for problem A and 
# 1000
# −
# 30
# ⋅
# 4
# =
# 880
# 1000−30⋅4=880 points for problem B. Thus, total 
# 460
# +
# 880
# =
# 1340
# 460+880=1340 points for both the problems.

# If Chef attempts in the order 
# B
# →
# A
# B→A then he submits Problem B after 
# 10
# 10 minutes and Problem A after 
# 30
# 30 minutes.
# Thus, he gets 
# 1000
# −
# 10
# ⋅
# 4
# =
# 960
# 1000−10⋅4=960 points for Problem B and 
# 500
# −
# 30
# ⋅
# 2
# =
# 440
# 500−30⋅2=440 points for Problem A. Thus total 
# 960
# +
# 440
# =
# 1400
# 960+440=1400 points for both the problems.

# So, Chef will attempt in the order 
# B
# →
# A
# B→A and thus obtain 
# 1400
# 1400 points.

def solve():
    X, Y = map(int, input().split())
    
    score_A_then_B = max(0, 500 - X * 2) + max(0, 1000 - (X + Y) * 4)
    score_B_then_A = max(0, 1000 - Y * 4) + max(0, 500 - (X + Y) * 2)
    
    print(max(score_A_then_B, score_B_then_A))

T = int(input())
for _ in range(T):
    solve()

# ==============================================================================================

# leetcode problem




# 120. Triangle
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        return dp[0]
    

    # ⏱️ Time & Space Complexity

# Time: O(n²) — we process each number once

# Space: O(n) — we use one list (dp) the size of the last row

# ==============================================================================================