# # code chef problem 


# Weights
# Chef is playing with weights. He has an object weighing 
# W
# W units. He also has three weights each of 
# X
# ,
# Y
# ,
# X,Y, and 
# Z
# Z units respectively. Help him determine whether he can measure the exact weight of the object with one or more of these weights.

# If it is possible to measure the weight of object with one or more of these weights, print YES, otherwise print NO.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of single line containing a four positive integers 
# W
# ,
# X
# ,
# Y
# ,
# W,X,Y, and 
# Z
# Z.
# Output Format
# For each test case, output on a new line YES if it is possible to measure the weight of object with one or more of these weights, otherwise print NO.

# You may print each character of the string in either uppercase or lowercase (for example, the strings yes, YES, Yes, and yeS will all be treated as identical).

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
# W
# ,
# X
# ,
# Y
# ,
# Z
# ≤
# 10
# 5
# 1≤W,X,Y,Z≤10 
# 5
 
# Sample 1:
# Input
# Output
# 4
# 5 2 1 6
# 7 9 7 2
# 20 8 10 12
# 20 10 11 12
# NO
# YES
# YES
# NO
# Explanation:
# Test Case 
# 1
# 1: It is not possible to measure 
# 5
# 5 units using any combination of given weights.

# Test Case 
# 2
# 2: Chef can use the second weight of 
# 7
# 7 units to measure the object exactly.

# Test Case 
# 3
# 3: Chef can use combination of first and third weights to measure 
# 8
# +
# 12
# =
# 20
# 8+12=20 units.

# Test Case 
# 4
# 4: Chef cannot measure 
# 20
# 20 units of weight using any combination of given weights.

# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a==b or a==c or a==d or a==b+c or a==c+d or a==b+d or a==b+c+d:
        print("YES")
    else:
        print("NO")


# ================================================================================
# leet code problem

# 3541. Find Most Frequent Vowel and Consonant
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.
 

# Example 1:

# Input: s = "successes"

# Output: 6

# Explanation:

# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.
# Example 2:

# Input: s = "aeiaeia"

# Output: 3

# Explanation:

# The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
# There are no consonants in s. Hence, maximum consonant frequency = 0.
# The output is 3 + 0 = 3.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters only.


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        max_vowel = max([freq[ch] for ch in freq if ch in vowels], default=0)
        max_consonant = max([freq[ch] for ch in freq if ch not in vowels], default=0)
        return max_vowel + max_consonant


# Example usage:# s = "successes"
# Output: 6 (2 for 'e' and 4 for 's')
# s = "aeiaeia"
# Output: 3 (3 for 'a' and 0 for consonants)