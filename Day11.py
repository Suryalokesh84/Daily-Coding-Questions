#  COde Chef problem



# Bath in Winters
# A geyser has a capacity of 
# X
# X litres of water and a bucket has a capacity of 
# Y
# Y litres of water.

# One person requires exactly 
# 2
# 2 buckets of water to take a bath. Find the maximum number of people that can take bath using water from one completely filled geyser..

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers 
# X
# ,
# Y
# X,Y.
# Output Format
# For each test case, output the maximum number of people that can take bath.

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
# Sample 1:
# Input
# Output
# 4
# 10 6
# 25 1
# 100 10
# 30 40
# 0
# 12
# 5
# 0
# Explanation:
# Test Case 
# 1
# 1: One bucket has a capacity of 
# 6
# 6 litres. This means that one person requires 
# 2
# ⋅
# 6
# =
# 12
# 2⋅6=12 litres of water to take a bath. Since this is less than the total water present in geyser, 
# 0
# 0 people can take bath.

# Test Case 
# 2
# 2: One bucket has a capacity of 
# 1
# 1 litre. This means that one person requires 
# 2
# ⋅
# 1
# =
# 2
# 2⋅1=2 litres of water to take a bath. The total amount of water present in geyser is 
# 25
# 25 litres. Thus, 
# 12
# 12 people can take bath. Note that 
# 1
# 1 litre water would remain unused in the geyser.

# Test Case 
# 3
# 3: One bucket has a capacity of 
# 10
# 10 litres. This means that one person requires 
# 2
# ⋅
# 10
# =
# 20
# 2⋅10=20 litres of water to take a bath. The total amount of water present in geyser is 
# 100
# 100 litres. Thus, 
# 5
# 5 people can take bath. Note that 
# 0
# 0 litres of water would remain unused in the geyser after this.

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(x // (2 * y))
# Test Case 
# 4
# leetcode problem

# 498. Diagonal Traverse
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        for d in range(m + n - 1):
            temp = []
            r = 0 if d < n else d - n + 1
            c = d - r
            
            while r < m and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        
        return result
