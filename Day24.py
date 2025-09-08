# X Jumps
# Chef is currently standing at stair 
# 0
# 0 and he wants to reach stair numbered 
# X
# X.

# Chef can climb either 
# Y
# Y steps or 
# 1
# 1 step in one move.
# Find the minimum number of moves required by him to reach exactly the stair numbered 
# X
# X.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of a single line of input containing two space separated integers 
# X
# X and 
# Y
# Y denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.
# Output Format
# For each test case, output the minimum number of moves required by him to reach exactly the stair numbered 
# X
# X.

# Constraints
# 1
# ≤
# T
# ≤
# 500
# 1≤T≤500
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
# 4 2
# 8 3
# 3 4
# 2 1
# 2
# 4
# 3
# 2
# Explanation:
# Test case 
# 1
# 1: Chef can make 
# 2
# 2 moves and climb 
# 2
# 2 steps in each move to reach stair numbered 
# 4
# 4.

# Test case 
# 2
# 2: Chef can make a minimum of 
# 4
# 4 moves. He can climb 
# 3
# 3 steps in 
# 2
# 2 of those moves and 
# 1
# 1 step each in remaining 
# 2
# 2 moves to reach stair numbered 
# 8
# 8.

# Test case 
# 3
# 3: Chef can make 
# 3
# 3 moves and climb 
# 1
# 1 step in each move to reach stair numbered 
# 3
# 3.

# Test case 
# 4
# 4: Chef can make 
# 2
# 2 moves and climb 
# 1
# 1 step in each move to reach stair numbered 
# 2
# 2.
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x % y == 0:
        print(x // y)
    else:
        print(x // y + x % y)
    # Example usage:
    # Input:
    # 4
    # 4 2
    # 8 3
    # 3 4
    # 2 1
    # Output:
    # 2
    # 4
    # 3
    # 2
# Explanation:
    # Test case 1: Chef can make 2 moves and climb 2 steps in each move to reach stair numbered 4.
    
    # Test case 2: Chef can make a minimum of 4 moves. He can climb 3 steps in 2 of those moves and 1 step each in remaining 2 moves to reach stair numbered 8.
    
    # Test case 3: Chef can make 3 moves and climb 1 step in each move to reach stair numbered 3.
    
    # Test case 4: Chef can make 2 moves and climb 1 step in each move to reach stair numbered 2.

# ==========================            ==========================  
# ✅ 2. Factorial of a Number

Iteration

def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_iter(5))  # 120



# =================================================================================
# 1317. Convert Integer to the Sum of Two No-Zero Integers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
 

# Constraints:

# 2 <= n <= 104