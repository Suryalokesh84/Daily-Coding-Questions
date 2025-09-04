# # code chef problem
# Finding Square Roots
# In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages .

# Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions. So here's your chance.

# Input
# The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

# Output

# For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.

# Constraints

# 1<=T<=20
# 1<=N<=10000

# Sample 1:
# Input

# Output
# 3
# 10
# 5
# 10000
# 3
# 2
# 100

import math

t = int(input())
for _ in range(t):
    n = int(input())
    sqrt_n = int(math.sqrt(n))
    print(sqrt_n)
# Example usage:
# Input:
# 3
# 10
# 5
# 10000
# Output:
# 3
# 2
# 100
# Explanation:
# The square root of 10 is approximately 3.16, which rounds down to 3.
# The square root of 5 is approximately 2.23, which rounds down to 2.
# The square root of 10000 is exactly 100.  


# ================================================================================
# leet code problem
# 3516. Find Closest Person
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given three integers x, y, and z, representing the positions of three people on a number line:

# x is the position of Person 1.
# y is the position of Person 2.
# z is the position of Person 3, who does not move.
# Both Person 1 and Person 2 move toward Person 3 at the same speed.

# Determine which person reaches Person 3 first:

# Return 1 if Person 1 arrives first.
# Return 2 if Person 2 arrives first.
# Return 0 if both arrive at the same time.
# Return the result accordingly.

 

# Example 1:

# Input: x = 2, y = 7, z = 4

# Output: 1

# Explanation:

# Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
# Person 2 is at position 7 and can reach Person 3 in 3 steps.
# Since Person 1 reaches Person 3 first, the output is 1.

# Example 2:

# Input: x = 2, y = 5, z = 6

# Output: 2

# Explanation:

# Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
# Person 2 is at position 5 and can reach Person 3 in 1 step.
# Since Person 2 reaches Person 3 first, the output is 2.

# Example 3:

# Input: x = 1, y = 5, z = 3

# Output: 0

# Explanation:

# Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
# Person 2 is at position 5 and can reach Person 3 in 2 steps.
# Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.

 

# Constraints:

# 1 <= x, y, z <= 100