# # pyramid qustion
# Problem Statement:
# Given an array of integers of size N.
# For each ith element in the array,
# calculate the absolute difference between the count of numbers that are to the left of i and are strictly greater than ith element, 
# and the count of numbers that are to the right of i 
# and are strictly lesser than ith element.
# Example 1: 
# Input: N = 5 A[] = {5, 4, 3, 2, 1} 
# Output: 4 2024 
# Explanation: We can see that the required number for the 1st element is 10-41 = 4 
# Example 2: Input: N = 5 A[] = {1, 2, 3, 4, 5} Output: 00000 
# Explanation: There is no greater element on the left for any element and no lesser element on the right. 
# Sample TestCases: Sample Input 1: 5 54321 54321 Sample Output 1: 42024 Sample Input 2: 5 12345 
# Sample Output 2: 00000 Constraints: 1≤ N ≤100 -1000 ≤ arr[i] ≤ 1000 Array can contain duplicate elements.
# For example: Test 
# Input Result Sample Test Case 1 5 5 4 3 2 1 4 2 0 2 4 
# Sample Test Case 2 5 00000 1 2 3 4 5


def compute_difference(N, A):
    result = []
    for i in range(N):
        left_greater = sum(1 for j in range(i) if A[j] > A[i])
        right_lesser = sum(1 for j in range(i+1, N) if A[j] < A[i])
        result.append(abs(left_greater - right_lesser))
    return result

N = int(input())
A = list(map(int, input().split()))

output = compute_difference(N, A)
print(*output)
# ======================================================================================================================
# code chef problem
# Too many Floors
# Chef and Chefina are residing in a hotel.

# There are 
# 10
# 10 floors in the hotel and each floor consists of 
# 10
# 10 rooms.

# Floor 
# 1
# 1 consists of room numbers 
# 1
# 1 to 
# 10
# 10.
# Floor 
# 2
# 2 consists of room numbers 
# 11
# 11 to 
# 20
# 20.
# …
# …
# Floor 
# i
# i consists of room numbers 
# 10
# ⋅
# (
# i
# −
# 1
# )
# +
# 1
# 10⋅(i−1)+1 to 
# 10
# ⋅
# i
# 10⋅i.
# You know that Chef's room number is 
# X
# X while Chefina's Room number is 
# Y
# Y.
# If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers 
# X
# ,
# Y
# X,Y, the room numbers of Chef and Chefina respectively.
# Output Format
# For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

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
# ,
# Y
# ≤
# 100
# 1≤X,Y≤100
# X
# ≠
# Y
# X=Y
# Sample 1:
# Input
# Output
# 4
# 1 100
# 42 50
# 53 30
# 81 80
# 9
# 0
# 3
# 1
# Explanation:
# Test Case 
# 1
# 1: Since Room 
# 1
# 1 is on 
# 1
# s
# t
# 1 
# st
#   floor and Room 
# 100
# 100 is on 
# 10
# t
# h
# 10 
# th
#   floor, Chef needs to climb 
# 9
# 9 floors to reach Chefina's Room.

# Test Case 
# 2
# 2: Since Room 
# 42
# 42 is on 
# 5
# t
# h
# 5 
# th
#   floor and Room 
# 50
# 50 is also on 
# 5
# t
# h
# 5 
# th
#   floor, Chef does not need to climb any floor.

# Test Case 
# 3
# 3: Since Room 
# 53
# 53 is on 
# 6
# t
# h
# 6 
# th
#   floor and Room 
# 30
# 30 is on 
# 3
# r
# d
# 3 
# rd
#   floor, Chef needs to go down 
# 3
# 3 floors to reach Chefina's Room.

# Test Case 
# 4
# 4: Since Room 
# 81
# 81 is on 
# 9
# t
# h
# 9 
# th
#   floor and Room 
# 80
# 80 is on 
# 8
# t
# h
# 8 
# th
#   floor, Chef needs to go down 
# 1
# 1 floors to reach Chefina's Room.



import math

def solve():
    X, Y = map(int, input().split())
    floor_x = math.ceil(X / 10)
    floor_y = math.ceil(Y / 10)
    print(abs(floor_x - floor_y))

T = int(input())
for _ in range(T):
    solve()