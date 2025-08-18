# 📘 Problem: Test Score

# Chef has appeared in a test consisting of N problems.
# Each problem carries X marks.

# For each problem, Chef either receives X marks (if solved correctly) or 0 marks (if left/wrong).

# You need to determine whether it is possible for Chef to score exactly Y marks.

# Input Format

# The first line contains a single integer T — the number of test cases.

# Each test case contains three integers:

# N → number of problems

# X → marks for each problem

# Y → score Chef wants

# Output Format

# For each test case, output YES if Chef can achieve exactly Y marks, otherwise output NO.

# You can print each character in uppercase or lowercase (YES, Yes, yes → all valid).

# Constraints

# 1 ≤ T ≤ 100

# 1 ≤ N ≤ 10

# 1 ≤ X ≤ 10

# 0 ≤ Y ≤ N × X

# Sample Input
# 5
# 1 8 4
# 3 6 12
# 4 5 0
# 10 10 100
# 8 5 36

# Sample Output
# NO
# YES
# YES
# YES
# NO

# Explanation

# Case 1: N=1, X=8, Y=4 → Chef can only score 0 or 8, but not 4 → NO

# Case 2: N=3, X=6, Y=12 → Chef can score 12 by solving 2 problems correctly → YES

# Case 3: N=4, X=5, Y=0 → Chef can leave all problems and score 0 → YES

# Case 4: N=10, X=10, Y=100 → Chef can solve all 10 problems → YES

# Case 5: N=8, X=5, Y=36 → 36 is not divisible by 5 → NO



t = int(input())
for _ in range(t):
    N, X, Y = map(int, input().split())
    
    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")
