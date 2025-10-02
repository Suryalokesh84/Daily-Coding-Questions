# # leet code problem


# 3100. Water Bottles II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integers numBottles and numExchange.

# numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

# Drink any number of full water bottles turning them into empty bottles.
# Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
# Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

# Return the maximum number of water bottles you can drink.

 

# Example 1:


# Input: numBottles = 13, numExchange = 6
# Output: 15
# Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
# Example 2:


# Input: numBottles = 10, numExchange = 3
# Output: 13
# Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
 

# Constraints:

# 1 <= numBottles <= 100 
# 1 <= numExchange <= 100



class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1
        return total



# =====================================================================================









# Code
# Testcase
# Testcase
# Test Result
# 9. Palindrome Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 





class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

# =====================================================================================



