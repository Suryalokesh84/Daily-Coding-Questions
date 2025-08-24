# # code chef
# Flip the cards
# There are 
# N
# N cards on a table, out of which 
# X
# X cards are face-up and the remaining are face-down.

# In one operation, we can do the following:

# Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down and vice versa)
# What is the minimum number of operations we must perform so that all the cards face in the same direction (i.e. either all are face-up or all are face-down)?

# Input Format
# The first line contains a single integer 
# T
# T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two space-separated integers 
# N
# N and 
# X
# X — the total number of cards and the number of cards which are initially face-up.
# Output Format
# For each test case, output the minimum number of cards you must flip so that all the cards face in the same direction.

# Constraints
# 1
# ≤
# T
# ≤
# 5000
# 1≤T≤5000
# 2
# ≤
# N
# ≤
# 100
# 2≤N≤100
# 0
# ≤
# X
# ≤
# N
# 0≤X≤N
# Sample 1:
# Input
# Output
# 4
# 5 0
# 4 2
# 3 3
# 10 2
# 0
# 2
# 0
# 2
# Explanation:
# Test Case 1: All the cards are already facing down. Therefore we do not need to perform any operations.

# Test Case 2: 
# 2
# 2 cards are facing up and 
# 2
# 2 cards are facing down. Therefore we can flip the 
# 2
# 2 cards which are initially facing down.

# Test Case 3: All the cards are already facing up. Therefore we do not need to perform any operations.

# Test Case 4: 
# 2
# 2 cards are facing up and 
# 8
# 8 cards are facing down. Therefore we can flip the 
# 2
# 2 cards which are initially facing up


# solution:--

def solve():
    n, x = map(int, input().split())
    print(min(x, n - x))

t = int(input())
for _ in range(t):
    solve()


# Example usage:# Input:
# 4
# ------------------------------------------------------------------------------
# leetcode problem


# 1493. Longest Subarray of 1's After Deleting One Element
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left)
        return res