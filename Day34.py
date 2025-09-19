# # code chef problem

# Airlines
# An airline operates 
# X
# X aircraft every day. Each aircraft can carry up to 
# 100
# 100 passengers.
# One day, 
# N
# N passengers would like to travel to the same destination. What is the minimum number of new planes that the airline must buy to carry all 
# N
# N passengers?

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of a single line containing two space-separated integers 
# X
# X and 
# N
# N — the number of aircraft the airline owns and the number of passengers travelling, respectively.
# Output Format
# For each test case, output the minimum number of planes the airline needs to purchase.
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
# ≤
# 10
# 6
# 1≤X≤10 
# 6
 
# 1
# ≤
# N
# ≤
# 10
# 6
# 1≤N≤10 
# 6
 
# Sample 1:
# Input
# Output
# 3
# 4 600
# 3 523
# 8 245
# 2
# 3
# 0
# Explanation:
# Test case 
# 1
# 1: The airline needs at least 
# 6
# 6 planes to carry 
# 600
# 600 passengers. They already have 
# 4
# 4, so they must purchase 
# 2
# 2 more.

# Test case 
# 2
# 2: The airline needs at least 
# 6
# 6 planes to carry 
# 523
# 523 passengers. They already have 
# 3
# 3, so they must purchase 
# 3
# 3 more.

# Test case 
# 3
# 3: The airline needs at least 
# 3
# 3 planes to carry 
# 245
# 245 passengers. They already have 
# 8
# 8, so there's no need to purchase any more.


def solve():
    X, N = map(int, input().split())
    
    needed_planes = (N + 99) // 100  # Calculate total planes needed
    
    ans = max(0, needed_planes - X) # Find the difference between needed and owned
    print(ans)

T = int(input())
for _ in range(T):
    solve()

# Example usage:
# Input:    
# 3
# 4 600
# 3 523
# 8 245
# Output:
# 2

# Explanation:
# Test case 1: The airline needs at least 6 planes to carry 600 passengers. They already have 4, so they must purchase 2 more.      
# Test case 2: The airline needs at least 6 planes to carry 523 passengers. They already have 3, so they must purchase 3 more.
# Test case 3: The airline needs at least 3 planes to carry 245 passengers. They already have 8, so there's no need to purchase any more.



# # ========================================================================================
# # leetcode problem


# 3484. Design Spreadsheet
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

# Implement the Spreadsheet class:

# Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
# void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
# void resetCell(String cell) Resets the specified cell to 0.
# int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
# Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

 

# Example 1:

# Input:
# ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
# [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

# Output:
# [null, 12, null, 16, null, 25, null, 15]

# Explanation

# Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
# spreadsheet.getValue("=5+7"); // returns 12 (5+7)
# spreadsheet.setCell("A1", 10); // sets A1 to 10
# spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
# spreadsheet.setCell("B2", 15); // sets B2 to 15
# spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
# spreadsheet.resetCell("A1"); // resets A1 to 0
# spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)
 

# Constraints:

# 1 <= rows <= 103
# 0 <= value <= 105
# The formula is always in the format "=X+Y", where X and Y are either valid cell references or non-negative integers with values less than or equal to 105.
# Each cell reference consists of a capital letter from 'A' to 'Z' followed by a row number between 1 and rows.
# At most 104 calls will be made in total to setCell, resetCell, and getValue.
 

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 38,861/55K
# Acceptance Rate
# 70.7%
# Topics
# icon
# Companies
# Hint 1
# Hint 2
# Hint 3
# Hint 4
# Similar Questions
# Discussion (60)

# Choose a type



# Copyright © 2025 LeetCode. All rights reserved.

# 104


# 60


# 4480 Online
# Python3
# Auto





# 123456789
# class Spreadsheet:

#     def __init__(self, rows: int):
        

#     def setCell(self, cell: str, value: int) -> None:
        

#     def resetCell(self, cell: str) -> None:
        

# Saved
# Case 1

# ["Spreadsheet","getValue","setCell","getValue","setCell","getValue","resetCell","getValue"]
# [[3],["=5+7"],["A1",10],["=A1+6"],["B2",15],["=A1+B2"],["A1"],["=A1+B2"]]









class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid = [[0] * self.cols for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = cell[0], int(cell[1:]) - 1
        c = ord(col) - ord('A')
        self.grid[row][c] = value

    def resetCell(self, cell: str) -> None:
        col, row = cell[0], int(cell[1:]) - 1
        c = ord(col) - ord('A')
        self.grid[row][c] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split('+')
        return self._getOperandValue(x) + self._getOperandValue(y)

    def _getOperandValue(self, op: str) -> int:
        if op[0].isalpha():
            col, row = op[0], int(op[1:]) - 1
            c = ord(col) - ord('A')
            return self.grid[row][c]
        else:
            return int(op)
