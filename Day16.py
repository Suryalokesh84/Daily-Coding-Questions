# # CODE CHEF PROBLEM:
# # 1st Question -----------------------------------------------------------------------------
# Complementary Strand in a DNA
# You are given the sequence of Nucleotides of one strand of DNA through a string 
# S
# S of length 
# N
# N. 
# S
# S contains the character 
# A
# ,
# T
# ,
# C
# ,
# A,T,C, and 
# G
# G only.

# Chef knows that:

# A
# A is complementary to 
# T
# T.
# T
# T is complementary to 
# A
# A.
# C
# C is complementary to 
# G
# G.
# G
# G is complementary to 
# C
# C.
# Using the string 
# S
# S, determine the sequence of the complementary strand of the DNA.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# First line of each test case contains an integer 
# N
# N - denoting the length of string 
# S
# S.
# Second line contains 
# N
# N characters denoting the string 
# S
# S.
# Output Format
# For each test case, output the string containing 
# N
# N characters - sequence of nucleotides of the complementary strand.

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
# ≤
# 100
# 1≤N≤100
# S
# S contains A, T, C, and G only
# Sample 1:
# Input
# Output
# 4
# 4
# ATCG
# 4
# GTCC
# 5
# AAAAA
# 3
# TAC
# TAGC
# CAGG
# TTTTT
# ATG
# Explanation:
# Test case 
# 1
# 1: Based on the rules, the complements of A, T, C, and G are T, A, G, and C respectively. Thus, the complementary string of the given string ATCG is TAGC.

# Test case 
# 2
# 2: Based on the rules, the complements of G, T, and C are C, A, and G respectively. Thus, the complementary string of the given string GTCC is CAGG.

# Test case 
# 3
# 3: Based on the rules, the complement of A is T. Thus, the complementary string of the given string AAAAA is TTTTT.

# Test case 
# 4
# 4: Based on the rules, the complements of T, A, and C are A, T, and G respectively. Thus, the complementary string of the given string TAC is ATG.


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    complement = ''
    for char in s:
        if char == 'A':
            complement += 'T'
        elif char == 'T':
            complement += 'A'
        elif char == 'C':
            complement += 'G'
        elif char == 'G':
            complement += 'C'
    print(complement)
# Example usage:
# Input:
# 4
# 4
# ATCG
# 4
# GTCC
# 5
# AAAAA
# 3
# TAC
# Output:
# TAGC
# CAGG
# TTTTT
# ATG
# Explanation:
# Test case 1: Based on the rules, the complements of A, T, C
# and G are T, A, G, and C respectively. Thus, the complementary string of the given string ATCG is TAGC.

# Test case 2: Based on the rules, the complements of G, T, and C are C, A, and G respectively. Thus, the complementary string of the given string GTCC is CAGG.
# Test case 3: Based on the rules, the complement of A is T. Thus, the complementary string of the given string AAAAA is TTTTT.
# Test case 4: Based on the rules, the complements of T, A, and C are A, T, and G respectively. Thus, the complementary string of the given string TAC is ATG.

# 2nd Question -----------------------------------------------------------------------------

# leetcode problem: 
# 37. Sudoku Solver
# Hard
# Topics
# premium lock icon
# Companies
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.