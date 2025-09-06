# Blackjack
# Chef is playing a variant of Blackjack, where 
# 3
# 3 numbers are drawn and each number lies between 
# 1
# 1 and 
# 10
# 10 (with both 
# 1
# 1 and 
# 10
# 10 inclusive). Chef wins the game when the sum of these 
# 3
# 3 numbers is exactly 
# 21
# 21.

# Given the first two numbers 
# A
# A and 
# B
# B, that have been drawn by Chef, what should be 
# 3
# 3-rd number that should be drawn by the Chef in order to win the game?

# Note that it is possible that Chef cannot win the game, no matter what is the 
# 3
# 3-rd number. In such cases, report 
# −
# 1
# −1 as the answer.

# Input Format
# The first line will contain an integer 
# T
# T - number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers 
# A
# A and 
# B
# B - the first and second number drawn by the Chef.
# Output Format
# For each testcase, output the 
# 3
# 3-rd number that should be drawn by the Chef in order to win the game. Output 
# −
# 1
# −1 if it is not possible for the Chef to win the game.

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# A
# ,
# B
# ≤
# 10
# 1≤A,B≤10
# Sample 1:
# Input
# Output
# 3
# 1 10
# 1 5
# 4 9
# 10
# -1
# 8
# Explanation:
# Test case 
# 1
# 1: The first two numbers are 
# 1
# 1 and 
# 10
# 10. If the third number will be 
# 10
# 10, the resulting sum will be 
# 1
# +
# 10
# +
# 10
# =
# 21
# 1+10+10=21. So Chef will win the game if the third number is 
# 10
# 10.

# Test case 
# 2
# 2: The first two numbers are 
# 1
# 1 and 
# 5
# 5. There is no number between 
# 1
# 1 and 
# 10
# 10, that can make the resulting sum 
# 21
# 21. Hence, the answer will be 
# −
# 1
# −1 in this test case.

# solution


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = 21 - (a + b)
    if 1 <= c <= 10:
        print(c)
    else:
        print(-1)

# Example usage:
# Input:
# 3
# 1 10
# 1 5
# 4 9
# Output:
# 10
# -1
# 8
# Explanation:
# In the first test case, the third number should be 10 to make the sum
# equal to 21 (1 + 10 + 10 = 21).
# In the second test case, there is no number between 1 and 10 that can
# make the sum equal to 21, so the output is -1.
# In the third test case, the third number should be 8 to make the sum
# equal to 21 (4 + 9 + 8 = 21).

# =========================================================================================================
# Day 22        

# 3495. Minimum Operations to Make Array Elements Zero
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D array queries, where queries[i] is of the form [l, r]. Each queries[i] defines an array of integers nums consisting of elements ranging from l to r, both inclusive.

# In one operation, you can:

# Select two integers a and b from the array.
# Replace them with floor(a / 4) and floor(b / 4).
# Your task is to determine the minimum number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.

 

# Example 1:

# Input: queries = [[1,2],[2,4]]

# Output: 3

# Explanation:

# For queries[0]:

# The initial array is nums = [1, 2].
# In the first operation, select nums[0] and nums[1]. The array becomes [0, 0].
# The minimum number of operations required is 1.
# For queries[1]:

# The initial array is nums = [2, 3, 4].
# In the first operation, select nums[0] and nums[2]. The array becomes [0, 3, 1].
# In the second operation, select nums[1] and nums[2]. The array becomes [0, 0, 0].
# The minimum number of operations required is 2.
# The output is 1 + 2 = 3.

# Example 2:

# Input: queries = [[2,6]]

# Output: 4

# Explanation:

# For queries[0]:

# The initial array is nums = [2, 3, 4, 5, 6].
# In the first operation, select nums[0] and nums[3]. The array becomes [0, 3, 4, 1, 6].
# In the second operation, select nums[2] and nums[4]. The array becomes [0, 3, 1, 1, 1].
# In the third operation, select nums[1] and nums[2]. The array becomes [0, 0, 0, 1, 1].
# In the fourth operation, select nums[3] and nums[4]. The array becomes [0, 0, 0, 0, 0].
# The minimum number of operations required is 4.
# The output is 4.

 

# Constraints:

# 1 <= queries.length <= 105
# queries[i].length == 2
# queries[i] == [l, r]
# 1 <= l < r <= 109



import math

class Solution:
    def minOperations(self, queries):
        limits = []
        x, steps = 1, 1
        while x <= 10**9:
            nxt = min(10**9, 4*x - 1)
            limits.append((x, nxt, steps))
            x *= 4
            steps += 1

        def calc_sum(n):
            if n <= 0: return 0
            res = 0
            for lo, hi, step in limits:
                if n < lo: break
                res += (min(n, hi) - lo + 1) * step
            return res

        ans = 0
        for l, r in queries:
            total_steps = calc_sum(r) - calc_sum(l-1)
            ans += (total_steps + 1) // 2
        return ans
