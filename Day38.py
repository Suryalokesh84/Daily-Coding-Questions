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