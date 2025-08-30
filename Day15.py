# # code chef problem
# Chess Ratings
# Alice has recently started playing Chess. Her current rating is 
# X
# X. She noticed that when she wins a game, her rating increases by 
# 8
# 8 points.

# Can you help Alice in finding out the minimum number of games she needs to win in order to make her rating greater than or equal to 
# Y
# Y?

# Input Format
# The first line of input will contain an integer 
# T
# T — the number of test cases. The description of 
# T
# T test cases follows.
# The first line of each test case contains two integers 
# X
# X and 
# Y
# Y, as described in the problem statement.
# Output Format
# For each test case, output the minimum number of games that Alice needs to win in order to make her rating greater than or equal to 
# Y
# Y.

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
# X
# ≤
# Y
# ≤
# 10
# 4
# 1≤X≤Y≤10 
# 4
 
# Sample 1:
# Input
# Output
# 4
# 10 10
# 10 17
# 10 18
# 10 19
# 0
# 1
# 1
# 2
# Explanation:
# Test case 
# 1
# 1: Since Alice's current rating 
# X
# X is already equal to her desired rating 
# Y
# Y, she doesn't need to win any game.

# Test case 
# 2
# 2: Alice's current rating is 
# 10
# 10. After winning 
# 1
# 1 game, her rating will become 
# 10
# +
# 8
# =
# 18
# 10+8=18, which is greater than her desired rating of 
# 17
# 17. Thus, she has to win at least 
# 1
# 1 game.

# Test case 
# 3
# 3: Alice's current rating is 
# 10
# 10. After winning 
# 1
# 1 game, her rating will become 
# 10
# +
# 8
# =
# 18
# 10+8=18, which is equal to her desired rating of 
# 18
# 18. Thus, she has to win at least 
# 1
# 1 game.

# Test case 
# 4
# 4: Alice's current rating is 
# 10
# 10. After winning 
# 1
# 1 game, her rating will become 
# 18
# 18, which is less than her desired rating of 
# 19
# 19. She will need to win one more game in order to make her rating 
# 26
# 26, which is greater than 
# 19
# 19. Thus, she has to win at least 
# 2
# 2 games.

import math

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        diff = Y - X
        ans = math.ceil(diff / 8)
        print(int(ans))
# Example usage:
# Input:
# 4
# 10 10
# 10 17
# 10 18
# 10 19
# Output:
# 0
# 1 
# 1
# 2
# Explanation:
# Test case 1: Since Alice's current rating X is already equal to her desired rating
# Y, she doesn't need to win any game.
# Test case 2: Alice's current rating is 10. After winning 1 game, her rating will become 10 + 8 = 18, which is greater than her desired rating of 17. Thus, she has to win at least 1 game.
# Test case 3: Alice's current rating is 10. After winning 1 game, her rating will become 10 + 8 = 18, which is equal to her desired rating of 18. Thus, she has to win at least 1 game.
# Test case 4: Alice's current rating is 10. After winning 1 game, her rating will become 18, which is less than her desired rating of 19. She will need to win one more game in order to make her rating 26, which is greater than 19. Thus, she has to win at least 2 games.  
# 

# ===========================================================================================
# second problem


# leetcode problem

# Code


# Testcase
# Testcase
# Test Result
# 36. Valid Sudoku
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board):
        # Use sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
        
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True
