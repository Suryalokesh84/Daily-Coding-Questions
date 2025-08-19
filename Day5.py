# code chef 
#   question





# Test Score
# In a test, there are 
# N
# N problems, each carrying 
# X marks.
# In each problem, Chef either received 
# X
# X marks or 
# 0
# 0 marks.

# Determine whether is it possible for Chef to achieve exactly 
# Y
# Y marks.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of three integers 
# N
# ,
# X
# ,
# N,X, and 
# Y
# Y, the number of problems, the maximum score for each problem, and the score Chef wants.
# Output Format
# For each test case, output YES if Chef can achieve exactly 
# Y
# Y marks, NO otherwise.

# You can print each character of the string in uppercase or lowercase. For example, the strings Yes, YES, yes, and yEs, are all considered identical.

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# N
# ≤
# 10
# 1≤N≤10
# 1
# ≤
# X
# ≤
# 10
# 1≤X≤10
# 0
# ≤
# Y
# ≤
# N
# ⋅
# X
# 0≤Y≤N⋅X
# Sample 1:
# Input
# Output
# 5
# 1 8 4
# 3 6 12
# 4 5 0
# 10 10 100
# 8 5 36
# NO
# YES
# YES
# YES
# NO
# Explanation:
# Test case 
# 1
# 1: There is no way for Chef to score exactly 
# 4
# 4 marks.

# Test case 
# 2
# 2: Chef can score 
# 12
# 12 marks by receiving 
# 6
# 6 marks in 
# 2
# 2 problems and 
# 0
# 0 marks in 
# 1
# 1 problem.

# Test case 
# 3
# 3: Chef can score 
# 0
# 0 marks by receiving 
# 0
# 0 marks in each of the 
# 4
# 4 problems.

# Test case 
# 4
# 4: Chef can score 
# 100
# 100 marks by receiving 
# 10
# 10 marks in each of the 
# 10
# 10 problems.

# Test case 
# 5
# 5: There is no way for Chef to score exactly 
# 36
# 36 marks.
t = int(input())
for _ in range(t):
    N, X, Y = map(int, input().split())
    
    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")
# Example usage:
# Input: 1 8 4  




# question 2

# Jenga Night
# Chef hosts a party for his birthday. There are 
# N
# N people at the party. All these 
# N
# N people decide to play Jenga.

# There are 
# X
# X Jenga tiles available. In one round, all the players pick 
# 1
# 1 tile each and place it in the tower.
# The game is valid if:

# All the players have a tile in each round;
# All the tiles are used at the end.
# Given 
# N
# N and 
# X
# X, find whether the game is valid.

# Input Format
# First line will contain 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, containing two space-separated integers 
# N
# N and 
# X
# X representing the number of people at the party and the number of available tiles respectively.
# Output Format
# For each test case, output in a single line 
# YES
# YES if the game is valid, else output 
# NO
# NO.

# You may print each character of the string in uppercase or lowercase (for example, the strings 
# YeS
# YeS, 
# yEs
# yEs, 
# yes
# yes and 
# YES
# YES will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 10
# 4
# 1≤T≤10 
# 4
 
# 1
# ≤
# N
# ,
# X
# ≤
# 1000
# 1≤N,X≤1000
# Sample 1:
# Input
# Output
# 3
# 3 3
# 4 2
# 2 4
# YES
# NO
# YES
# Explanation:
# Test case 
# 1
# 1: The game will last for 
# 1
# 1 round after which the tiles will finish.

# Test case 
# 2
# 2: There are not enough Jenga tiles for everyone to place.

# Test case 
# 3
# 3: The game will last for 
# 2
# 2 rounds as after round 
# 2
# 2 all Jenga tiles are used.



t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if x % n == 0:
        print("YES")
    else:
        print("NO")