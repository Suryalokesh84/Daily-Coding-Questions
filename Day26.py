# # code chef problem
# Valentine is Coming
# Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.

# Chef has a total of 
# X
# X rupees and one chocolate costs 
# Y
# Y rupees. What is the maximum number of chocolates Chef can buy?

# Input Format
# First line will contain 
# T
# T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers 
# X
# ,
# Y
# X,Y - the amount Chef has and the cost of one chocolate respectively.
# Output Format
# For each test case, output the maximum number of chocolates Chef can buy.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# X
# ,
# Y
# ≤
# 100
# 1≤X,Y≤100
# Sample 1:
# Input
# Output
# 4
# 5 10
# 16 5
# 35 7
# 100 1
# 0
# 3
# 5
# 100
# Explanation:
# Test case-1: Chef has 
# 5
# 5 rupees but the cost of one chocolate is 
# 10
# 10 rupees. Therefore Chef can not buy any chocolates.

# Test case-2: Chef has 
# 16
# 16 rupees and the cost of one chocolate is 
# 5
# 5 rupees. Therefore Chef can buy at max 
# 3
# 3 chocolates since buying 
# 4
# 4 chocolates would cost 
# 20
# 20 rupees.

# Test case-3: Chef has 
# 35
# 35 rupees and the cost of one chocolate is 
# 7
# 7 rupees. Therefore Chef can buy at max 
# 5
# 5 chocolates for 
# 35
# 35 rupees.

# Test case-4: Chef has 
# 100
# 100 rupees and the cost of one chocolate is 
# 1
# 1 rupee. Therefore Chef can buy at max 
# 100
# 100 chocolates for 
# 100
# # 100 rupees.

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(X // Y)

    # =================================================================================
    # leetcode problem






# 1733. Minimum Number of People to Teach
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

# Example 1:

# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:

# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

# Constraints:

# 2 <= n <= 500
# languages.length == m
# 1 <= m <= 500
# 1 <= languages[i].length <= n
# 1 <= languages[i][j] <= n
# 1 <= u​​​​​​i < v​​​​​​i <= languages.length
# 1 <= friendships.length <= 500
# All tuples (u​​​​​i, v​​​​​​i) are unique
# languages[i] contains only unique values










    class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        know = [set(l) for l in languages]
        need = set()
        for u, v in friendships:
            if know[u-1].intersection(know[v-1]): 
                continue
            need.add(u-1)
            need.add(v-1)
        if not need: 
            return 0
        res = float("inf")
        for lang in range(1, n+1):
            cnt = 0
            for u in need:
                if lang not in know[u]:
                    cnt += 1
            res = min(res, cnt)
        return res
