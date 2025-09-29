# # code chef problem
# Cyclic Quadrilateral
# Read problem statements in Mandarin Chinese, Russian, and Vietnamese as well.
# You are given the sizes of angles of a simple quadrilateral (in degrees) 
# A
# A, 
# B
# B, 
# C
# C and 
# D
# D, in some order along its perimeter. Determine whether the quadrilateral is cyclic.

# Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 
# 180
# ∘
# 180 
# ∘
#  .

# Input
# The first line of the input contains a single integer 
# T
# T denoting the number of test cases. The description of 
# T
# T test cases follows.
# The first and only line of each test case contains four space-separated integers 
# A
# A, 
# B
# B, 
# C
# C and 
# D
# D.
# Output
# Print a single line containing the string "YES" if the given quadrilateral is cyclic or "NO" if it is not (without quotes).

# You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

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
# A
# ,
# B
# ,
# C
# ,
# D
# ≤
# 357
# 1≤A,B,C,D≤357
# A
# +
# B
# +
# C
# +
# D
# =
# 360
# A+B+C+D=360
# Sample 1:
# Input
# Output
# 3
# 10 20 30 300
# 10 20 170 160
# 179 1 179 1
# NO
# YES
# NO
# Explanation:
# Example case 1: The sum of two opposite angles 
# A
# +
# C
# =
# 10
# ∘
# +
# 30
# ∘
# ≠
# 180
# ∘
# A+C=10 
# ∘
#  +30 
# ∘
#  =180 
# ∘
#  .

# Example case 2: The sum of two opposite angles 
# A
# +
# C
# =
# 10
# ∘
# +
# 170
# ∘
# =
# 180
# ∘
# A+C=10 
# ∘
#  +170 
# ∘
#  =180 
# ∘
#   and 
# B
# +
# D
# =
# 20
# ∘
# +
# 160
# ∘
# =
# 180
# ∘
# B+D=20 
# ∘
#  +160 
# ∘
#  =180 
# ∘
#  .

# Example case 3: The sum of two opposite angles 
# B
# +
# D
# =
# 1
# ∘
# +
# 1
# ∘
# ≠
# 180
# ∘
# B+D=1 
# ∘
#  +1 
# ∘
#  =180 
# ∘
#  .


def solve():
    a, b, c, d = map(int, input().split())
    if a + c == 180 or b + d == 180:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()


# ====================================================================================================================



# leet code problem






# 1039. Minimum Score Triangulation of Polygon
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

# Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

# You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

# Return the minimum possible score that you can achieve with some triangulation of the polygon.

 

# Example 1:



# Input: values = [1,2,3]

# Output: 6

# Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

# Example 2:



# Input: values = [3,7,4,5]

# Output: 144

# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
# The minimum score is 144.

# Example 3:



# Input: values = [1,3,1,4,1,5]

# Output: 13

# Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

 

# Constraints:

# n == values.length
# 3 <= n <= 50
# 1 <= values[i] <= 100