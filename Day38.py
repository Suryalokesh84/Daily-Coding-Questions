# # Minimum Spanning Tree [Graphs]
# You are given a connected, undirected, weighted graph with N vertices and M edges. Your task is to find the weight of the Minimum Spanning Tree (MST) using either Kruskal’s Algorithm or Prim’s Algorithm. The MST of a graph is a subset of edges that connects all vertices together without cycles and with the minimum possible total edge weight.

# Input Format

# First line: Two integers N and M → number of vertices and edges. Next M lines: Three integers u v w, representing an undirected edge between u and v with weight w.

# Constraints

# 3 <= N <= 20

# Output Format

# Print the total weight of the MST.

# Sample Input 0

# 4 5
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4
# Sample Output 0

# MST weight = 19
# Explanation 0

# minimum spanning tree with the below edges

# 0->1 = 10 0->3 = 5 2->3 = 4

# 10+5+4 = 19

# Contest ends in 13 hours
# Submissions: 284
# Max Score: 10
# Difficulty: Medium
# Rate This Challenge:

    
# More
 
# 1
# ​

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            self.parent[yr] = xr
            return True
        return False

# Input reading
n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Kruskal's algorithm
edges.sort()
dsu = DSU(n)
mst_weight = 0

for w, u, v in edges:
    if dsu.union(u, v):
        mst_weight += w

print(f"MST weight = {mst_weight}")
# ======================================================================================================================
# code chef problem





# Speed Limit Test
# Alice is driving from her home to her office which is 
# A
# A kilometers away and will take her 
# X
# X hours to reach.
# Bob is driving from his home to his office which is 
# B
# B kilometers away and will take him 
# Y
# Y hours to reach.

# Determine who is driving faster, else, if they are both driving at the same speed print EQUAL.

# Input Format
# The first line will contain 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing four integers 
# A
# ,
# X
# ,
# B
# ,
# A,X,B, and 
# Y
# Y, the distances and and the times taken by Alice and Bob respectively.
# Output Format
# For each test case, if Alice is faster, print ALICE. Else if Bob is faster, print BOB. If both are equal, print EQUAL.

# You may print each character of the string in uppercase or lowercase (for example, the strings equal, equAL, EquAl, and EQUAL will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# A
# ,
# X
# ,
# B
# ,
# Y
# ≤
# 1000
# 1≤A,X,B,Y≤1000
# Sample 1:
# Input
# Output
# 3
# 20 6 20 5
# 10 3 20 6
# 9 1 1 1
# Bob
# Equal
# Alice
# Explanation:
# Test case 
# 1
# 1: Since Bob travels the distance between his office and house in 
# 5
# 5 hours, whereas Alice travels the same distance of 
# 20
# 20 kms in 
# 6
# 6 hours, BOB is faster.

# Test case 
# 2
# 2: Since Alice travels the distance of 
# 10
# 10 km between her office and house in 
# 3
# 3 hours and Bob travels a distance of 
# 20
# 20 km in 
# 6
# 6 hours, they have equal speeds.

# Test case 
# 3
# 3: Since Alice travels the distance of 
# 9
# 9 km between her office and house in 
# 1
# 1 hour and Bob travels only a distance of 
# 1
# 1 km in the same time, ALICE is faster.


def solve():
    A, X, B, Y = map(int, input().split())
    
    alice_speed = A / X
    bob_speed = B / Y
    
    if alice_speed > bob_speed:
        print("ALICE")
    elif bob_speed > alice_speed:
        print("BOB")
    else:
        print("EQUAL")

T = int(input())
for _ in range(T):
    solve()

    # ======================================================================================================================
    # LEET CODE PROBLEM







#     165. Compare Version Numbers
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
 

# Example 1:

# Input: version1 = "1.2", version2 = "1.10"

# Output: -1

# Explanation:

# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

# Example 2:

# Input: version1 = "1.01", version2 = "1.001"

# Output: 0

# Explanation:

# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 3:

# Input: version1 = "1.0", version2 = "1.0.0.0"

# Output: 0

# Explanation:

# version1 has less revisions, which means every missing revision are treated as "0".

 

# Constraints:

# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.


