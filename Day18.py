# # code chef problem
# Candy Distribution
# Chef has 
# N
# N candies. He has to distribute them to exactly 
# M
# M of his friends such that each friend gets equal number of candies and each friend gets even number of candies. Determine whether it is possible to do so.

# NOTE: Chef will not take any candies himself and will distribute all the candies.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers 
# N
# N and 
# M
# M, the number of candies and the number of friends.
# Output Format
# For each test case, the output will consist of a single line containing Yes if Chef can distribute the candies as per the conditions and No otherwise.

# You may print each character of the string in uppercase or lowercase (for example, the strings yes, Yes, yEs, and YES will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# N
# ,
# M
# ≤
# 1000
# 1≤N,M≤1000
# Sample 1:
# Input
# Output
# 4
# 9 3
# 4 1
# 4 2
# 8 3
# No
# Yes
# Yes
# No
# Explanation:
# Test case 
# 1
# 1: Since Chef has 
# 9
# 9 candies and 
# 3
# 3 friends, each friend will get 
# 9
# 3
# =
# 3
# 3
# 9
# ​
#  =3 candies. Since 
# 3
# 3 is not even, Chef doesn't satisfy the conditions.

# Test case 
# 2
# 2: Since Chef has 
# 4
# 4 candies and 
# 1
# 1 friend, each friend will get 
# 4
# 1
# =
# 4
# 1
# 4
# ​
#  =4 candies. Since 
# 4
# 4 is even, Chef satisfies all the conditions.

# Test case 
# 3
# 3: Since Chef has 
# 4
# 4 candies and 
# 2
# 2 friends, each friend will get 
# 4
# 2
# =
# 2
# 2
# 4
# ​
#  =2 candies. Since 
# 2
# 2 is even, Chef satisfies all the conditions.

# Test case 
# 4
# 4: Since Chef has 
# 8
# 8 candies and 
# 3
# 3 friends. Since Chef won't be able to distribute all the candies equally, Chef doe
# 
# s not satisfy all the conditions.

# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=a/b
    if c%2==0:
        print("Yes")
    else:
        print("No")






# #3025. Find the Number of Ways to Place People I
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

# Count the number of pairs of points (A, B), where

# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.

 

# Example 1:

# Input: points = [[1,1],[2,2],[3,3]]

# Output: 0

# Explanation:



# There is no way to choose A and B so A is on the upper left side of B.

# Example 2:

# Input: points = [[6,2],[4,4],[2,6]]

# Output: 2

# Explanation:



# The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
# The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
# The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.
# Example 3:

# Input: points = [[3,1],[1,3],[1,1]]

# Output: 2

# Explanation:



# The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
# The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
# The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.
 

# Constraints:

# 2 <= n <= 50
# points[i].length == 2
# 0 <= points[i][0], points[i][1] <= 50
# All points[i] are distinct. 




class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        ans=0
        for i in range(n):
            for j in range(n):
                if points[i][0]<=points[j][0] and points[i][1]>=points[j][1] and (points[i][0]<points[j][0] or points[i][1]>points[j][1]):
                    ok=True
                    for k in range(n):
                        if i!=k and j!=k:
                            if points[i][0]<=points[k][0]<=points[j][0] and points[j][1]<=points[k][1]<=points[i][1]:
                                ok=False
                                break
                    if ok: ans+=1
        return ans
    

# Example usage:
# points = [[6,2],[4,4],[2,6]]



# # ======================================================================
# Setting Up a MERN Stack Project
# To setup MERN stack we need to create a folder structure for both frontend and backend. Then we have to define database schema to store and retrieve data from the database.

# Follow the below steps to create a basic structure

# Step 1: After the code editor is installed, create a new project folder. Then go to the project folder in command prompt/terminal and type below commands to create folder for frontend and backend 

# mkdir frontend
# mkdir backend
# Step 2: Navigate to the frontend folder using the command

# cd frontend
# Step 3: Initialize a React Project using the command

# npx create-react-app
# Step 4: Now navigate to the backend folder using the command

# cd..
# cd backend
# Step 5: Initialize the project backend using the command

# npm init -y
# Step 6: Install Express and other backend dependencies using the command

# npm i mongodb express cors dotenv 
# After following all the above steps a basic structure for MERN Stack application is created.