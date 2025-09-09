# # code chef     problem
# Chessboard Distance
# The Chessboard Distance for any two points 
# (
# X
# 1
# ,
# Y
# 1
# )
# (X 
# 1
# ​
#  ,Y 
# 1
# ​
#  ) and 
# (
# X
# 2
# ,
# Y
# 2
# )
# (X 
# 2
# ​
#  ,Y 
# 2
# ​
#  ) on a Cartesian plane is defined as 
# m
# a
# x
# (
# ∣
# X
# 1
# −
# X
# 2
# ∣
# ,
# ∣
# Y
# 1
# −
# Y
# 2
# ∣
# )
# max(∣X 
# 1
# ​
#  −X 
# 2
# ​
#  ∣,∣Y 
# 1
# ​
#  −Y 
# 2
# ​
#  ∣).

# You are given two points 
# (
# X
# 1
# ,
# Y
# 1
# )
# (X 
# 1
# ​
#  ,Y 
# 1
# ​
#  ) and 
# (
# X
# 2
# ,
# Y
# 2
# )
# (X 
# 2
# ​
#  ,Y 
# 2
# ​
#  ). Output their Chessboard Distance.

# Note that, 
# ∣
# P
# ∣
# ∣P∣ denotes the absolute value of integer 
# P
# P. For example, 
# ∣
# −
# 4
# ∣
# =
# 4
# ∣−4∣=4 and 
# ∣
# 7
# ∣
# =
# 7
# ∣7∣=7.

# Input Format
# First line will contain 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input containing 
# 4
# 4 space separated integers - 
# X
# 1
# ,
# Y
# 1
# ,
# X
# 2
# ,
# Y
# 2
# X 
# 1
# ​
#  ,Y 
# 1
# ​
#  ,X 
# 2
# ​
#  ,Y 
# 2
# ​
#   - as defined in the problem statement.
# Output Format
# For each test case, output in a single line the chessboard distance between 
# (
# X
# 1
# ,
# Y
# 1
# )
# (X 
# 1
# ​
#  ,Y 
# 1
# ​
#  ) and 
# (
# X
# 2
# ,
# Y
# 2
# )
# (X 
# 2
# ​
#  ,Y 
# 2
# ​
#  )

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
# 1
# ,
# Y
# 1
# ,
# X
# 2
# ,
# Y
# 2
# ≤
# 10
# 5
# 1≤X 
# 1
# ​
#  ,Y 
# 1
# ​
#  ,X 
# 2
# ​
#  ,Y 
# 2
# ​
#  ≤10 
# 5
 
# Subtasks
# Subtask #1 (100 points): original constraints

# Sample 1:
# Input
# Output
# 3
# 2 4 5 1
# 5 5 5 3
# 1 4 3 3
# 3
# 2
# 2
# Explanation:
# In the first case, the distance between 
# (
# 2
# ,
# 4
# )
# (2,4) and 
# (
# 5
# ,
# 1
# )
# (5,1) is 
# m
# a
# x
# (
# ∣
# 2
# −
# 5
# ∣
# ,
# ∣
# 4
# −
# 1
# ∣
# )
# =
# m
# a
# x
# (
# ∣
# −
# 3
# ∣
# ,
# ∣
# 3
# ∣
# )
# =
# 3
# max(∣2−5∣,∣4−1∣)=max(∣−3∣,∣3∣)=3.

# In the second case, the distance between 
# (
# 5
# ,
# 5
# )
# (5,5) and 
# (
# 5
# ,
# 3
# )
# (5,3) is 
# m
# a
# x
# (
# ∣
# 5
# −
# 5
# ∣
# ,
# ∣
# 5
# −
# 3
# ∣
# )
# =
# m
# a
# x
# (
# ∣
# 0
# ∣
# ,
# ∣
# 2
# ∣
# )
# =
# 2
# max(∣5−5∣,∣5−3∣)=max(∣0∣,∣2∣)=2.

# In the third case, the distance between 
# (
# 1
# ,
# 4
# )
# (1,4) and 
# (
# 3
# ,
# 3
# )
# (3,3) is 
# m
# a
# x
# (
# ∣
# 1
# −
# 3
# ∣
# ,
# ∣
# 4
# −
# 3
# ∣
# )
# =
# m
# a
# x
# (
# ∣
# −
# 2
# ∣
# ,
# ∣
# 1
# ∣
# )
# =
# 2
# max(∣1−3∣,∣4−3∣)=max(∣−2∣,∣1∣)=2.

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    print(max(abs(x1 - x2), abs(y1 - y2)))

t = int(input())
for _ in range(t):
    solve()


    # ================================================================
# 2327. Number of People Aware of a Secret
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# On day 1, one person discovers a secret.

# You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

# Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 6, delay = 2, forget = 4
# Output: 5
# Explanation:
# Day 1: Suppose the first person is named A. (1 person)
# Day 2: A is the only person who knows the secret. (1 person)
# Day 3: A shares the secret with a new person, B. (2 people)
# Day 4: A shares the secret with a new person, C. (3 people)
# Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
# Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
# Example 2:

# Input: n = 4, delay = 1, forget = 3
# Output: 6
# Explanation:
# Day 1: The first person is named A. (1 person)
# Day 2: A shares the secret with B. (2 people)
# Day 3: A and B share the secret with 2 new people, C and D. (4 people)
# Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)
 

# Constraints:

# 2 <= n <= 1000
# 1 <= delay < forget <= n

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0
        for i in range(2, n + 1):
            if i - delay >= 1:
                share = (share + dp[i - delay]) % mod
            if i - forget >= 1:
                share = (share - dp[i - forget]) % mod
            dp[i] = share
        return sum(dp[n - forget + 1: n + 1]) % mod
