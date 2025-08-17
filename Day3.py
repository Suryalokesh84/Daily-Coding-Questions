# 35. Search Insert Position
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left





# 📝 Question:

# Write a Python program to check whether a given string is a palindrome or not.
# (A palindrome is a word, number, or phrase that reads the same backward as forward. Example: "madam", "121".)

# Input Example:

# madam


# Output Example:

# Palindrome

def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

# Example usage
word = input("Enter a string: ")
print(is_palindrome(word))



# 📝 Question:

# Write a Python program to find the largest number in a list without using the built-in max() function.

# Input Example:

# [10, 25, 4, 99, 67]


# Output Example:

# Largest number is: 99


def find_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

# Example usage
numbers = [10, 25, 4, 99, 67]
print("Largest number is:", find_largest(numbers))
