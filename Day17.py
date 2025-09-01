# Chef and Water Bottles
# Chef has 
# N
# N empty bottles where each bottle has a capacity of 
# X
# X litres.
# There is a water tank in Chefland having 
# K
# K litres of water. Chef wants to fill the empty bottles using the water in the tank.

# Assuming that Chef does not spill any water while filling the bottles, find out the maximum number of bottles Chef can fill completely.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, three integers 
# N
# ,
# X
# ,
# N,X, and 
# K
# K.
# Output Format
# For each test case, output in a single line answer, the maximum number of bottles Chef can fill completely.

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
# ,
# X
# ≤
# 10
# 5
# 1≤N,X≤10 
# 5
 
# 0
# ≤
# K
# ≤
# 10
# 5
# 0≤K≤10 
# 5
 
# Sample 1:
# Input
# Output
# 3
# 5 2 8
# 10 5 4
# 3 1 4
# 4
# 0
# 3
# Explanation:
# Test Case 
# 1
# 1: The amount of water in the tank is 
# 8
# 8 litres. The capacity of each bottle is 
# 2
# 2 litres. Hence, 
# 4
# 4 water bottles can be filled completely.

# Test Case 
# 2
# 2: The amount of water in the tank is 
# 4
# 4 litres. The capacity of each bottle is 
# 5
# 5 litres. Hence, no water bottle can be filled completely.

# Test Case 
# 3
# 3: The amount of water in the tank is 
# 4
# 4 litres. The capacity of each bottle is 
# 1
# 1 litre. Chef has 
# 3
# 3 bottles available. He can fill all these bottles completely using 
# 3
# 3 litres of water.

def solve():
    N, X, K = map(int, input().split())
    print(min(N, K // X))

T = int(input())
for _ in range(T):
    solve()



# ----------------------------------------------------------------------
# leet code problem
# 1792. Maximum Average Pass Ratio
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
# Example 2:

# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485
 

# Constraints:

# 1 <= classes.length <= 105
# classes[i].length == 2
# 1 <= passi <= totali <= 105
# 1 <= extraStudents <= 105

from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def delta(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = [(-delta(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            d, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-delta(p, t), p, t))
        
        return sum(p / t for _, p, t in heap) / len(classes)
# Example usage:
# classes = [[1,2],[3,5],[2,2]] 
# extraStudents = 2
# Output: 0.78333
