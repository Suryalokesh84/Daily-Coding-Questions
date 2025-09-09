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