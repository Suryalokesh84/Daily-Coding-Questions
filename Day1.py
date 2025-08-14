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





#2nd Question


#Binary to decimal conversion
a=tuple(map(int,input().split()))
length=len(a)-1
add=0
for i in a:
    add+=(2**length)*i
    length-=1
print(add)
# Example usage:
# a = (1, 0, 1, 1)  # Represents binary 1011
# Output: 11 (decimal equivalent of binary 1011)



#dynamic progaraming fibonaci

def fib(n,arr):
    if n==0 or n==1:
        return n
    if arr[n]!=-1:
        return arr[n]
    result=fib(n-1,arr)+fib(n-2,arr)
    arr[n]=result
    return result
n=5
arr=[-1]*(n+1)
arr[0]=0
arr[1]=1
print(fib(n,arr))
print(arr)
# Example usage:
# n = 5 # Output: 5 (the 5th Fibonacci number)
# arr will contain the Fibonacci sequence up to n, e.g., [0, 1  , 1, 2, 3, 5]   