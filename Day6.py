 # Leet code 
# 349. Intersection of Two Arrays
# Easy
# Topics
# premium lock icon
# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        intersection_set = set()
        
        for num in nums2:
            if num in set1:
                intersection_set.add(num)
                
        return list(intersection_set)
    


    # # Example usage:    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]



# -------------------------------------------------------------------------------------------------------
    # streak question

    # 1277. Count Square Submatrices with All Ones
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    count += matrix[i][j]
                    
        return count