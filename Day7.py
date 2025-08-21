# # ✅ Question:

# A player in discus throw is given 3 throws, and the throw with the longest distance is regarded as their final score.

# You are given the distances for all 3 throws of a player. Determine the final score of the player.

# Input Format:

# The first line will contain an integer T (number of test cases).

# Each test case contains 3 integers A, B, C — the distances in each throw.

# Output Format:

# For each test case, print the final score of the player.

# Constraints:

# 1 ≤ T ≤ 100

# 1 ≤ A, B, C ≤ 100

# Sample Input:
# 3
# 10 15 8
# 32 32 32
# 82 45 54

# Sample Output:
# 15
# 32
# 82

# Number of test cases
T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    # Final score is the maximum distance
    print(max(A, B, C))

