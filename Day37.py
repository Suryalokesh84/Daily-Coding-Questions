# # pyramid qustion
# Problem Statement:
# Given an array of integers of size N.
# For each ith element in the array,
# calculate the absolute difference between the count of numbers that are to the left of i and are strictly greater than ith element, 
# and the count of numbers that are to the right of i 
# and are strictly lesser than ith element.
# Example 1: 
# Input: N = 5 A[] = {5, 4, 3, 2, 1} 
# Output: 4 2024 
# Explanation: We can see that the required number for the 1st element is 10-41 = 4 
# Example 2: Input: N = 5 A[] = {1, 2, 3, 4, 5} Output: 00000 
# Explanation: There is no greater element on the left for any element and no lesser element on the right. 
# Sample TestCases: Sample Input 1: 5 54321 54321 Sample Output 1: 42024 Sample Input 2: 5 12345 
# Sample Output 2: 00000 Constraints: 1≤ N ≤100 -1000 ≤ arr[i] ≤ 1000 Array can contain duplicate elements.
# For example: Test 
# Input Result Sample Test Case 1 5 5 4 3 2 1 4 2 0 2 4 
# Sample Test Case 2 5 00000 1 2 3 4 5