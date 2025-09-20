# # code chef problem
# Self Defence Training
# After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

# The only condition for a woman to be eligible for the special training is that she must be between 
# 10
# 10 and 
# 60
# 60 years of age, inclusive of both 
# 10
# 10 and 
# 60
# 60.

# Given the ages of 
# N
# N women in his village, please help San Te find out how many of them are eligible for the special training.

# Input Format
# The first line of input contains a single integer 
# T
# T, denoting the number of test cases. The description of 
# T
# T test cases follows.
# The first line of each test case contains a single integer 
# N
# N, the number of women.
# The second line of each test case contains 
# N
# N space-separated integers 
# A
# 1
# ,
# A
# 2
# ,
# .
# .
# .
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,...,A 
# N
# ​
#  , the ages of the women.
# Output Format
# For each test case, output in a single line the number of women eligible for self-defence training.

# Constraints
# 1
# ≤
# T
# ≤
# 20
# 1≤T≤20
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# 1
# ≤
# A
# i
# ≤
# 100
# 1≤A 
# i
# ​
#  ≤100
# Sample 1:
# Input
# Output
# 3
# 3
# 15 23 65
# 3
# 15 62 16
# 2
# 35 9
# 2
# 2
# 1
# Explanation:
# Test Case 
# 1
# 1: Out of the women, only the 
# 1
# s
# t
# 1 
# st
#   and 
# 2
# n
# d
# 2 
# nd
#   women are eligible for the training because their ages lie in the interval 
# [
# 10
# ,
# 60
# ]
# [10,60]. Hence the answer is 2.

# Test Case 
# 2
# 2: Only the 
# 1
# s
# t
# 1 
# st
#   and 
# 3
# r
# d
# 3 
# rd
#   women are eligible for the training because their ages lie in the interval 
# [
# 10
# ,
# 60
# ]
# [10,60]. Hence the answer is again 2.

# Test Case 
# 3
# 3: Only the 
# 1
# s
# t
# 1 
# st
#   woman with age 
# 35
# 35 is eligible for the training. Hence the answer is 
# 1
# 1.


t = int(input())
for _ in range(t):
    n = int(input())
    ages = list(map(int, input().split()))
    count = 0
    for age in ages:
        if 10 <= age <= 60:
            count += 1
    print(count)