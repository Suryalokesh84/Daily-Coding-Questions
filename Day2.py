# ✅ 1. TCS NQT (2023) – Smallest Missing Positive
# Integer

# 🧩 Problem Statement:

# You are given an unsorted integer array. Your task is to find the smallest positive integer that is not present in the array.

# 📥 Input:

# ● An array of integers arr[] (can include negative numbers and duplicates).

# ● Size of array: 1 <= N <= 10^5

# 📤 Output:

# ● Print the smallest missing positive integer.

# 📌 Example:

# Input: [3, 4, -1, 1]

# Output: 2

# Input: [1, 2, 0]

# Output: 3

# ✅ Constraints:

# ● Time Complexity ≤ O(n)

# ● Use constant extra space if possible.


a = list(map(int, input().split()))
a.sort()

List = []
for i in a:
    if i > 0:
        List.append(i)

if len(List) == 0:
    print(1)  # if no positive numbers, return 1
else:
    b = len(List)
    c = List[b - 1] + 2
    for i in range(1, c):
        if i not in List:
            print(i)
            break






# ✅ 3. Wipro NLTH (2023) – Count Pairs with Even Sum
# 🧩 Problem Statement:

# Given an array of integers, count how many unique pairs (i, j) can be formed such that:

# ● i < j

# ● The sum of the pair is even

# 📥 Input:

# ● An integer array arr[]

# ● Length 1 <= N <= 10^4

# 📤 Output:

# ● An integer representing the count of valid pairs

# 📌 Example: makefile CopyEdit

# Input: [1, 2, 3, 4]

# Output: 2

# Explanation: Even pairs are → (1, 3), (2, 4)

# 🔍 Hint:

# Even + Even = Even

# Odd + Odd = Even

# (So count number of even and odd elements separately and calculate combinations)

# 📌 Example: makefile CopyEdit

# Input:

# arr = [1, 2, 3, 4, 5]

# d = 2

# Output:

# [3, 4, 5, 1, 2]

# 💡 Constraints:

# ● Use slicing or queue-like behavior.

# ● Time complexity ≤ O(n)