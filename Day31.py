# # code chef problem
# Chef Eren
# Chef is a very big fan of Eren Yeager.

# In the last season of Attack on Titan, there were 
# N
# N episodes numbered from 
# 1
# 1 to 
# N
# N.
# Each even indexed episode was 
# A
# A minutes long and each odd indexed episode was 
# B
# B minutes long.

# Calculate the total duration (in minutes) of the last season.

# Input Format
# The first line of input contains a single integer 
# T
# T, the number of test cases.
# The first and only line of each test case contains three integers 
# N
# N, 
# A
# ,
# A, and 
# B
# B, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.
# Output Format
# For each test case, print a single integer on a new line, the total duration of the last season in minutes.

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
# 60
# 1≤N≤60
# 1
# ≤
# A
# ,
# B
# ≤
# 60
# 1≤A,B≤60
# Sample 1:
# Input
# Output
# 3
# 1 2 2
# 2 3 4
# 4 20 30
# 2
# 7
# 100
# Explanation:
# Test case 
# 1
# 1: There is only one episode, so there is 
# 1
# 1 odd-indexed episode, and 
# 0
# 0 even-indexed episode. The total duration of the season 
# =
# 0
# ⋅
# A
# +
# 1
# ⋅
# B
# =
# 0
# ⋅
# 2
# +
# 1
# ⋅
# 2
# =
# 2
# =0⋅A+1⋅B=0⋅2+1⋅2=2.

# Test case 
# 2
# 2: There are two episodes with indices 
# {
# 1
# ,
# 2
# }
# {1,2}. Thus, there is 
# 1
# 1 odd-indexed episode 
# (
# {
# 1
# }
# )
# ({1}), and 
# 1
# 1 even-indexed episode 
# (
# {
# 2
# }
# )
# ({2}). The total duration of the season 
# =
# 1
# ⋅
# A
# +
# 1
# ⋅
# B
# =
# 1
# ⋅
# 3
# +
# 1
# ⋅
# 4
# =
# 7
# =1⋅A+1⋅B=1⋅3+1⋅4=7.

# Test case 
# 3
# 3: There are four episodes with indices 
# {
# 1
# ,
# 2
# ,
# 3
# ,
# 4
# }
# {1,2,3,4}. Thus, there are 
# 2
# 2 odd-indexed episodes 
# (
# {
# 1
# ,
# 3
# }
# )
# ({1,3}), and 
# 2
# 2 even-indexed episodes 
# (
# {
# 2
# ,
# 4
# }
# )
# ({2,4}). The total duration of the season 
# =
# 2
# ⋅
# A
# +
# 2
# ⋅
# B
# =
# 2
# ⋅
# 20
# +
# 2
# ⋅
# 30
# =
# 100
# =2⋅A+2⋅B=2⋅20+2⋅30=100.

def solve():
    n, a, b = map(int, input().split())
    
    num_odd = (n + 1) // 2
    num_even = n // 2
    
    total_duration = num_odd * b + num_even * a
    print(total_duration)

t = int(input())
for _ in range(t):
    solve()


# Example usage:
# Input:
# 3
# 1 2 2
# 2 3 4
# 4 20 30
# Output:
# 2

# Explanation:
# Test case 1: There is only one episode, so there is 1 odd-index
# episode ( {1} ) and 0 even-indexed episode. The total duration of the season = 0⋅A + 1⋅B = 0⋅2 + 1⋅2 = 2.
# Test case 2: There are two episodes with indices {1, 2}. Thus, there is 1 odd-indexed episode ({1}), and 1 even-indexed episode ({2}). The total duration of the season = 1⋅A + 1⋅B = 1⋅3 + 1⋅4 = 7.
# Test case 3: There are four episodes with indices {1, 2, 3, 4}. Thus, there are 2 odd-indexed episodes ({1, 3}), and 2 even-indexed episodes ({2, 4}). The total duration of the season = 2⋅A + 2⋅B = 2⋅20 + 2⋅30 = 100.
# Test case 2: There is no unused memory in the phone. Chef has to first delete one of the apps from the phone and then only he can install the



# ============================================================================
# leet code problem




# 1935. Maximum Number of Words You Can Type
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

# Example 1:

# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
# Example 2:

# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
# Example 3:

# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.
 

# Constraints:

# 1 <= text.length <= 104
# 0 <= brokenLetters.length <= 26
# text consists of words separated by a single space without any leading or trailing spaces.
# Each word only consists of lowercase English letters.
# brokenLetters consists of distinct lowercase English letters.











class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)  
        count = 0
        
        for word in text.split(): 
            if not any(ch in broken_set for ch in word):  
                count += 1
        return count