# # CODE CHEF PROBLEM
# Mario and Bullet
# Mario's bullet moves at 
# X
# X pixels per frame. He wishes to shoot a goomba standing 
# Y
# Y pixels away from him. The goomba does not move.

# Find the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least 
# Z
# Z seconds from now.

# Input Format
# The first line of input will contain an integer 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing three space-separated integers 
# X
# ,
# Y
# ,
# X,Y, and 
# Z
# Z.
# Output Format
# For each test case, output in a single line the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least 
# Z
# Z seconds from now.

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
# ,
# Y
# ,
# Z
# ≤
# 100
# 1≤X,Y,Z≤100
# X
# X divides 
# Y
# Y
# Sample 1:
# Input
# Output
# 3
# 3 3 5
# 2 4 1
# 3 12 8
# 4
# 0
# 4
# Explanation:
# Test case 
# 1
# 1: The speed of the bullet is 
# 3
# 3 pixels per frame and the goomba is 
# 3
# 3 pixels away from Mario. Thus, it would take 
# 1
# 1 second for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least 
# 5
# 5 seconds. So, he should fire the bullet after 
# 4
# 4 seconds.

# Test case 
# 2
# 2: The speed of the bullet is 
# 2
# 2 pixels per frame and the goomba is 
# 4
# 4 pixels away from Mario. Thus, it would take 
# 2
# 2 seconds for the bullet to reach the goomba. Mario wants the bullet to reach the goomba after at least 
# 1
# 1 second. So, he should fire the bullet after 
# 0
# 0 seconds. Note that, this is the minimum time after which he can shoot a bullet.

# Test case 
# 3
# 3: The speed of the bullet is 
# 3
# 3 pixels per frame and the goomba is 
# 12
# 12 pixels away from Mario. Thus, it would take 
# 4
# 4 seconds for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least 
# 8
# 8 seconds. So, he should fire the bullet after 
# 4
# 4 seconds.

T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    wait_time = max(0, Z - Y // X)
    print(wait_time)

# # Example usage:
# # X = 3, Y = 12, Z = 8
# # Output: 4
# # Explanation: The speed of the bullet is 3 pixels per frame and the goomba is 12 pixels away from Mario. Thus, it would take 4 seconds for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least 8 seconds. So, he should fire the bullet after 4 seconds.


# ``````````````````````````````````````----------------------------------------`------------------------------------------------
# # 2nd Question`

# 3021. Alice and Bob Playing Flower Game
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.



# The game proceeds as follows:

# Alice takes the first turn.
# In each turn, a player must choose either one of the lane and pick one flower from that side.
# At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
# Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

# Alice must win the game according to the described rules.
# The number of flowers x in the first lane must be in the range [1,n].
# The number of flowers y in the second lane must be in the range [1,m].
# Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

 

# Example 1:

# Input: n = 3, m = 2
# Output: 3
# Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
# Example 2:

# Input: n = 1, m = 1
# Output: 0
# Explanation: No pairs satisfy the conditions described in the statement.
 

# Constraints:

# 1 <= n, m <= 105