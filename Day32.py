# # code chef problem
# Minimum number of coins
# Chef has infinite coins in denominations of rupees 
# 5
# 5 and rupees 
# 10
# 10.

# Find the minimum number of coins Chef needs, to pay exactly 
# X
# X rupees. If it is impossible to pay 
# X
# X rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only, print 
# −
# 1
# −1.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single integer 
# X
# X.
# Output Format
# For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly 
# X
# X rupees. If it is impossible to pay 
# X
# X rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only, print 
# −
# 1
# −1.

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
# ≤
# 1000
# 1≤X≤1000
# Subtasks
# Subtask 1 (100 points): Original constraints.
# Sample 1:
# Input
# Output
# 3
# 50
# 15
# 8
# 5
# 2
# -1
# Explanation:
# Test Case 
# 1
# 1: Chef would require at least 
# 5
# 5 coins to pay 
# 50
# 50 rupees. All these coins would be of rupees 
# 10
# 10.

# Test Case 
# 2
# 2: Chef would require at least 
# 2
# 2 coins to pay 
# 15
# 15 rupees. Out of these, 
# 1
# 1 coin would be of rupees 
# 10
# 10 and 
# 1
# 1 coin would be of rupees 
# 5
# 5.

# Test Case 
# 3
# 3: Chef cannot pay exactly 
# 8
# 8 rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only.

t = int(input())
for _ in range(t):
    x = int(input())
    if x % 5 != 0:
        print(-1)
    else:
        tens = x // 10
        fives = (x % 10) // 5
        print(tens + fives)
# Example usage:
# Input:
# 3
# 50
# 15
# 8
# Output:
# 5
# 2
# -1
# Explanation:
# Test Case 1: Chef would require at least 5 coins to pay 50 rupees.
# All these coins would be of rupees 10.
# Test Case 2: Chef would require at least 2 coins to pay 15 rupees. Out of these, 1 coin would be of rupees 10 and 1 coin would be of rupees 5.
# Test Case 3: Chef cannot pay exactly 8 rupees in denominations of rupees 5 and 10 only.


# =======================================================================================

# leet code problem
# 2197. Replace Non-Coprime Numbers in Array
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of integers nums. Perform the following steps:

# Find any two adjacent numbers in nums that are non-coprime.
# If no such numbers are found, stop the process.
# Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
# Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

# The test cases are generated such that the values in the final array are less than or equal to 108.

# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

 

# Example 1:

# Input: nums = [6,4,3,2,7,6,2]
# Output: [12,7,6]
# Explanation: 
# - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
# - (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
# - (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
# - (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [12,7,6].
# Note that there are other ways to obtain the same resultant array.
# Example 2:

# Input: nums = [2,2,1,1,3,3,3]
# Output: [2,1,1,3]
# Explanation: 
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
# - (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [2,1,1,3].
# Note that there are other ways to obtain the same resultant array.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# The test cases are generated such that the values in the final array are less than or equal to 108.


from math import gcd, lcm
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                num = lcm(stack.pop(), num)
            stack.append(num)
        return stack
