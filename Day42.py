# # code chef problem


# Pass or Fail
# Chef is struggling to pass a certain college course.

# The test has a total of 
# N
# N questions, each question carries 
# 3
# 3 marks for a correct answer and 
# −
# 1
# −1 for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got 
# X
# X questions correct and the rest of them incorrect. For Chef to pass the course he must score at least 
# P
# P marks.

# Will Chef be able to pass the exam or not?

# Input Format
# First line will contain 
# T
# T, number of testcases. Then the testcases follow.
# Each testcase contains of a single line of input, three integers 
# N
# ,
# X
# ,
# P
# N,X,P.
# Output Format
# For each test case output "PASS" if Chef passes the exam and "FAIL" if Chef fails the exam.

# You may print each character of the string in uppercase or lowercase (for example, the strings "pASs", "pass", "Pass" and "PASS" will all be treated as identical).

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
# 100
# 1≤N≤100
# 0
# ≤
# X
# ≤
# N
# 0≤X≤N
# 0
# ≤
# P
# ≤
# 3
# ⋅
# N
# 0≤P≤3⋅N
# Sample 1:
# Input
# Output
# 3
# 5 2 3
# 5 2 4
# 4 0 0
# PASS
# FAIL
# FAIL
# Explanation:
# Test case 
# 1
# 1: Chef gets 
# 2
# 2 questions correct giving him 
# 6
# 6 marks and since he got 
# 3
# 3 questions incorrect so he faces a penalty of 
# −
# 3
# −3. So Chef's final score is 
# 3
# 3 and the passing marks are also 
# 3
# 3, so he passes the exam :)

# Test case 
# 2
# 2: Chef's total marks are 
# 3
# 3 and since the passing marks are 
# 4
# 4, Chef fails the test :(

# Test case 
# 3
# 3: Chef got all the problems wrong and thus his total score is 
# −
# 4
# −4. Since the passing marks are 
# 0
# 0, Chef fails the exam 


T = int(input())
for _ in range(T):
    N, X, P = map(int, input().split())
    score = (3 * X) - (N - X)
    if score >= P:
        print("PASS")
    else:
        print("FAIL")



# ====================================================================================================================


# leetcode problem
















# 976. Largest Perimeter Triangle
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106