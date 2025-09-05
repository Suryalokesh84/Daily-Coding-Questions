# # code chef problem
# The Last Levels
# Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

# There are 
# X
# X levels remaining in the game, and each level takes Chef 
# Y
# Y minutes to complete. To protect against eye strain, Chef also decides that every time he completes 
# 3
# 3 levels, he will take a 
# Z
# Z minute break from playing. Note that there is no need to take this break if the game has been completed.

# How much time (in minutes) will it take Chef to complete the game?

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# The first and only line of input will contain three space-separated integers 
# X
# X, 
# Y
# Y, and 
# Z
# Z.
# Output Format
# For each test case, output on a new line the answer — the length of Chef's gaming session.

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
# 5
# ≤
# Y
# ≤
# 100
# 5≤Y≤100
# 5
# ≤
# Z
# ≤
# 15
# 5≤Z≤15
# Sample 1:
# Input
# Output
# 4
# 2 12 10
# 3 12 10
# 7 20 8
# 24 45 15
# 24
# 36
# 156
# 1185
# Explanation:
# Test case 1: 2 12 10

# X = 2 (2 levels remain)
# Y = 12 (each level takes 12 minutes)
# Z = 10 (Chef would take a 10-minute break every 3 levels, but since there are only 2 levels, no break is needed)
# Since there are only 2 levels, and no break is needed (because Chef takes a break only after every 3 levels).

# The total time = X × Y = 2 × 12 = 24 minutes.

# Test case 3: 7 20 8

# X = 7 (7 levels remain)
# Y = 20 (each level takes 20 minutes)
# Z = 8 (Chef takes an 8-minute break after every 3 levels)
# Now, let's break this down:
# Chef completes the first 3 levels: 3 x 20 = 60 minutes.
# After completing these 3 levels, Chef takes an 8-minute break.
# Chef completes another 3 levels: 3 x 20 = 60 minutes.
# After completing these 3 levels, Chef takes another 8-minute break.
# Now, Chef completes the remaining 1 level: 1 x 20 = 20 minutes.

# So, the total time = 60 + 8 + 60 + 8 + 20 = 156 minutes.


# cook your dish here
for i in range(int(input())):
    X,Y,Z=map(int,input().split())
    total_time=X*Y
    rest=X//3
    if X%3==0:
        rest-=1
        print(total_time+rest*Z)
    else:
        print(total_time+rest*Z)
# Example usage:
# Input:
# 4
# 2 12 10       
# 3 12 10
# 7 20 8
# 24 45 15
# Output:
# 24
# 36
# 156
# 1185
# Explanation:
# For the first test case, Chef completes 2 levels without needing a break, so the
# total time is 2 * 12 = 24 minutes.
# For the second test case, Chef completes 3 levels and takes one break, so the total time is 3 * 12 + 10 = 36 minutes.
# For the third test case, Chef completes 7 levels, taking two breaks after the first
# 3 levels each, so the total time is 7 * 20 + 2 * 8 = 156 minutes.
# For the fourth test case, Chef completes 24 levels, taking 8 breaks after every
# 3 levels, so the total time is 24 * 45 + 8 * 15 = 1185 minutes.


# ================================================================================`


# leet code problem
# 2749. Minimum Operations to Make the Integer Zero
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integers num1 and num2.

# In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

# Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

# If it is impossible to make num1 equal to 0, return -1.

 

# Example 1:

# Input: num1 = 3, num2 = -2
# Output: 3
# Explanation: We can make 3 equal to 0 with the following operations:
# - We choose i = 2 and subtract 22 + (-2) from 3, 3 - (4 + (-2)) = 1.
# - We choose i = 2 and subtract 22 + (-2) from 1, 1 - (4 + (-2)) = -1.
# - We choose i = 0 and subtract 20 + (-2) from -1, (-1) - (1 + (-2)) = 0.
# It can be proven, that 3 is the minimum number of operations that we need to perform.
# Example 2:

# Input: num1 = 5, num2 = 7
# Output: -1
# Explanation: It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
 

# Constraints:

# 1 <= num1 <= 109
# -109 <= num2 <= 109