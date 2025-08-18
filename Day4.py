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




# 📘 Problem: Maximum Marks in Exam

# Chef is preparing for an exam.
# The exam has N problems, each problem carries X marks, but Chef has K minutes to attempt them.

# Solving 1 problem takes M minutes.

# Chef can either solve the problem fully (and get X marks) or skip it.

# Chef cannot solve a problem partially.

# You need to determine the maximum marks Chef can score in the exam.

# Input Format

# The first line contains a single integer T — the number of test cases.

# Each test case contains four integers:

# N → number of problems

# X → marks per problem

# K → total time available (in minutes)

# M → time required to solve one problem

# Output Format

# For each test case, output a single integer — the maximum marks Chef can score.

# Constraints

# 1 ≤ T ≤ 100

# 1 ≤ N ≤ 100

# 1 ≤ X ≤ 10

# 1 ≤ K, M ≤ 1000

# Sample Input
# 4
# 5 4 15 3
# 10 2 8 5
# 6 10 25 4
# 7 5 100 20

# Sample Output
# 20
# 2
# 60
# 35

# Explanation

# Case 1: N=5, X=4, K=15, M=3

# Each problem takes 3 minutes, so in 15 minutes Chef can solve 5 problems.

# Each problem gives 4 marks → 5 × 4 = 20

# Case 2: N=10, X=2, K=8, M=5

# Each problem takes 5 minutes, but Chef only has 8 minutes.

# So Chef can solve only 1 problem → 1 × 2 = 2

# Case 3: N=6, X=10, K=25, M=4

# Max problems possible in 25 minutes = 25 // 4 = 6 (but only 6 problems exist).

# 6 × 10 = 60

# Case 4: N=7, X=5, K=100, M=20

# Max problems possible in 100 minutes = 100 // 20 = 5 (out of 7 available).

# 5 × 5 = 35

T = int(input())   # number of test cases

for _ in range(T):
    N, X, K, M = map(int, input().split())

    # Max number of problems Chef can attempt within K minutes
    max_problems_by_time = K // M

    # But Chef cannot solve more than N problems
    problems_solved = min(N, max_problems_by_time)

    # Total marks = problems solved × marks per problem
    print(problems_solved * X)
# ✅ Sample Run
# Input:
# Copy
# Edit
# 4
# 5 4 15 3
# 10 2 8 5
# 6 10 25 4
# 7 5 100 20