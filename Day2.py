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
