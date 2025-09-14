# # code chef problem
# Chef and his Apps
# Chef's phone has a total storage of 
# S
# S MB. Also, Chef has 
# 2
# 2 apps already installed on his phone which occupy 
# X
# X MB and 
# Y
# Y MB respectively.

# He wants to install another app on his phone whose memory requirement is 
# Z
# Z MB. For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

# Input Format
# The first line contains a single integer 
# T
# T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains four integers 
# S
# ,
# X
# ,
# Y
# S,X,Y and 
# Z
# Z — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.
# Output Format
# For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# S
# ≤
# 500
# 1≤S≤500
# 1
# ≤
# X
# ≤
# Y
# ≤
# S
# 1≤X≤Y≤S
# X
# +
# Y
# ≤
# S
# X+Y≤S
# Z
# ≤
# S
# Z≤S
# Sample 1:
# Input
# Output
# 4
# 10 1 2 3
# 9 4 5 1
# 15 5 10 15
# 100 20 30 75
# 0
# 1
# 2
# 1
# Explanation:
# Test Case 1: The unused memory in the phone is 
# 7
# 7 MB. Therefore Chef can install the 
# 3
# 3 MB app without deleting any app.

# Test Case 2: There is no unused memory in the phone. Chef has to first delete one of the apps from the phone and then only he can install the 
# 1
# 1 MB app.

# Test Case 3: There is no unused memory in the phone. Chef has to first delete both the apps from the phone and then only he can install the 
# 15
# 15 MB app.

# Test Case 4: The unused memory in the phone is 
# 50
# 50 MB. Chef has to first delete the 
# 30
# 30 MB app from the phone and then only he can install the 
# 75
# 75 MB app.

def solve():
    S, X, Y, Z = map(int, input().split())
    
    available_space = S - (X + Y)
    
    if available_space >= Z:
        print(0)
    elif X >= Z - available_space or Y >= Z - available_space:
        print(1)
    else:
        print(2)

T = int(input())
for _ in range(T):
    solve()



    # ========================================================================
    
# # LeetCode problem
# 966. Vowel Spellchecker
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:

# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

# Example 1:

# Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# Example 2:

# Input: wordlist = ["yellow"], queries = ["YellOw"]
# Output: ["yellow"]
 

# Constraints:

# 1 <= wordlist.length, queries.length <= 5000
# 1 <= wordlist[i].length, queries[i].length <= 7
# wordlist[i] and queries[i] consist only of only English letters.












class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        lower_map = {}
        vowel_map = {}
        vowels = set('aeiou')

        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word)

        for word in wordlist:
            lower = word.lower()
            if lower not in lower_map:
                lower_map[lower] = word
            dev = devowel(lower)
            if dev not in vowel_map:
                vowel_map[dev] = word

        res = []
        for q in queries:
            if q in words:
                res.append(q)
            else:
                lower = q.lower()
                if lower in lower_map:
                    res.append(lower_map[lower])
                else:
                    dev = devowel(lower)
                    if dev in vowel_map:
                        res.append(vowel_map[dev])
                    else:
                        res.append("")
        return res
# Example usage:
# wordlist = ["KiTe","kite","hare","Hare"]
# queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# ========================================================================
