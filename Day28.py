# # code chef problem
# Water Mixing
# Chef is setting up a perfect bath for himself. He has 
# X
# X litres of hot water and 
# Y
# Y litres of cold water.
# The initial temperature of water in his bathtub is 
# A
# A degrees. On mixing water, the temperature of the bathtub changes as following:

# The temperature rises by 
# 1
# 1 degree on mixing 
# 1
# 1 litre of hot water.
# The temperature drops by 
# 1
# 1 degree on mixing 
# 1
# 1 litre of cold water.
# Determine whether he can set the temperature to 
# B
# B degrees for a perfect bath.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of four space-separated integers 
# A
# ,
# B
# ,
# X
# ,
# A,B,X, and 
# Y
# Y — the initial temperature of bathtub, the desired temperature of bathtub, the amount of hot water in litres, and the amount of cold water in litres respectively.
# Output Format
# For each test case, output on a new line, YES if Chef can get the desired temperature for his bath, and NO otherwise.

# You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 2000
# 1≤T≤2000
# 20
# ≤
# A
# ,
# B
# ≤
# 40
# 20≤A,B≤40
# 0
# ≤
# X
# ,
# Y
# ≤
# 20
# 0≤X,Y≤20
# Sample 1:
# Input
# Output
# 4
# 24 25 2 0
# 37 37 2 9
# 30 20 10 9
# 30 31 0 20
# YES
# YES
# NO
# NO
# Explanation:
# Test case 
# 1
# 1: The initial temperature of water is 
# 24
# 24 and the desired temperature is 
# 25
# 25. Chef has 
# 2
# 2 litres of hot water. He can add 
# 1
# 1 litre hot water in the tub and change the temperature to 
# 24
# +
# 1
# =
# 25
# 24+1=25 degrees.

# Test case 
# 2
# 2: The initial temperature of water is 
# 37
# 37 and the desired temperature is also 
# 37
# 37. Thus, Chef does not need to add any more water in the bathtub.

# Test case 
# 3
# 3: The initial temperature of water is 
# 30
# 30 and the desired temperature is 
# 20
# 20. Chef needs to add 
# 10
# 10 litres of cold water to reach the desired temperature. Since he only has 
# 9
# 9 litres of cold water, he cannot reach the desired temperature.

# Test case 
# 4
# 4: The initial temperature of water is 
# 30
# 30 and the desired temperature is 
# 31
# 31. Chef needs to add 
# 1
# 1 litre of hot water to reach the desired temperature. Since he has no hot water, he cannot reach the desired temperature.


t = int(input())
for _ in range(t):
    A, B, X, Y = map(int, input().split())
    if A - Y <= B <= A + X:
        print("YES")
    else:
        print("NO")

# =========================================================================================
# leet code problem




# 3227. Vowels Game in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Alice and Bob are playing a game on a string.

# You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

# On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
# On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.
# The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

# Return true if Alice wins the game, and false otherwise.

# The English vowels are: a, e, i, o, and u.

 

# Example 1:

# Input: s = "leetcoder"

# Output: true

# Explanation:
# Alice can win the game as follows:

# Alice plays first, she can delete the underlined substring in s = "leetcoder" which contains 3 vowels. The resulting string is s = "der".
# Bob plays second, he can delete the underlined substring in s = "der" which contains 0 vowels. The resulting string is s = "er".
# Alice plays third, she can delete the whole string s = "er" which contains 1 vowel.
# Bob plays fourth, since the string is empty, there is no valid play for Bob. So Alice wins the game.
# Example 2:

# Input: s = "bbcd"

# Output: false

# Explanation:
# There is no valid play for Alice in her first turn, so Alice loses the game.

 

# Constraints:

# 1 <= s.length <= 105
# s consists only of lowercase English letters.













class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        return any(c in vowels for c in s)
