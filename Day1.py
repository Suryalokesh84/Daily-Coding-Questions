# Repetitive Addition Of Digits

# Problem Statement: You are given a positive integer n, you need to add all the digits of n and create a new number. Perform this operation until the resultant number has only one digit in it. Return the final number obtained after performing the given operation.

# Examples:

# Input: n = 1234

# Output: 1

# Explanation: Step 1: 1 + 2 + 3 + 4 = 10. Step 2: 1 + 0 = 1

# Input: n = 5674

# Output: 4

# Explanation: Step 1: 5 + 6 + 7 + 4 = 22. Step 2: 2 + 2 = 4

# Input: n = 9

# Output: 9

# Explanation: Since 9 is a single-digit number hence we return 9.

# Sample TestCases: Sample Input 1: 1234

# Sample Output 1: 1

# Constraints: 0 ≤ n ≤ 300

# For example:

# Test Input Result Sample Test Case 1 1234 1

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
n=int(input())
print(digital_root(n))
# Example usage:
# n = 1234
