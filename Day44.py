# # code chef problem



# Too many items
# Chef bought 
# N
# N items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.

# 1
# 1 polybag can contain at most 
# 10
# 10 items. What is the minimum number of polybags needed by Chef?

# Input Format
# The first line will contain an integer 
# T
# T - number of test cases. Then the test cases follow.
# The first and only line of each test case contains an integer 
# N
# N - the number of items bought by Chef.
# Output Format
# For each test case, output the minimum number of polybags required.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# N
# ≤
# 1000
# 1≤N≤1000
# Sample 1:
# Input
# Output
# 3
# 20
# 24
# 99
# 2
# 3
# 10
# Explanation:
# Test case-1: Chef will require 
# 2
# 2 polybags. Chef can fit 
# 10
# 10 items in the first and second polybag each.

# Test case-2: Chef will require 
# 3
# 3 polybags. Chef can fit 
# 10
# 10 items in the first and second polybag each and fit the remaining 
# 4
# 4 items in the third polybag.




def solve():
    n = int(input())
    print((n + 9) // 10)

t = int(input())
for _ in range(t):
    solve()
















#     # =================================================================================================






# leet code problem
#     2221. Find Triangular Sum of an Array
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

# The triangular sum of nums is the value of the only element present in nums after the following process terminates:

# Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
# For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the triangular sum of nums.

 

# Example 1:


# Input: nums = [1,2,3,4,5]
# Output: 8
# Explanation:
# The above diagram depicts the process from which we obtain the triangular sum of the array.
# Example 2:

# Input: nums = [5]
# Output: 5
# Explanation:
# Since there is only one element in nums, the triangular sum is the value of that element itself.
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 9








class Solution:
    def triangularSum(self, nums):
        while len(nums) > 1:
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums[0]


