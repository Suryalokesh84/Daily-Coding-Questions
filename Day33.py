# # code chef problem``

# Minimum number of coins
# Chef has infinite coins in denominations of rupees 
# 5
# 5 and rupees 
# 10
# 10.

# Find the minimum number of coins Chef needs, to pay exactly 
# X
# X rupees. If it is impossible to pay 
# X
# X rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only, print 
# −
# 1
# −1.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single integer 
# X
# X.
# Output Format
# For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly 
# X
# X rupees. If it is impossible to pay 
# X
# X rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only, print 
# −
# 1
# −1.

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
# ≤
# 1000
# 1≤X≤1000
# Subtasks
# Subtask 1 (100 points): Original constraints.
# Sample 1:
# Input
# Output
# 3
# 50
# 15
# 8
# 5
# 2
# -1
# Explanation:
# Test Case 
# 1
# 1: Chef would require at least 
# 5
# 5 coins to pay 
# 50
# 50 rupees. All these coins would be of rupees 
# 10
# 10.

# Test Case 
# 2
# 2: Chef would require at least 
# 2
# 2 coins to pay 
# 15
# 15 rupees. Out of these, 
# 1
# 1 coin would be of rupees 
# 10
# 10 and 
# 1
# 1 coin would be of rupees 
# 5
# 5.

# Test Case 
# 3
# 3: Chef cannot pay exactly 
# 8
# 8 rupees in denominations of rupees 
# 5
# 5 and 
# 10
# 10 only.


t = int(input())
for _ in range(t):
    x = int(input())
    if x % 5 != 0:
        print(-1)
    else:
        tens = x // 10
        fives = (x % 10) // 5
        print(tens + fives)\
        

# ----------------------------------------------------------------------------


# # LEETCODE PROBLEMS

# 3408. Design Task Manager
# Medium
# Topics
# premium lock icon
# Companies
# There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

# Implement the TaskManager class:

# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

# Note that a user may be assigned multiple tasks.

 

# Example 1:

# Input:
# ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

# Output:
# [null, null, null, 3, null, null, 5]

# Explanation

# TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
# taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8); // Updates priority of task 102 to 8.
# taskManager.execTop(); // return 3. Executes task 103 for User 3.
# taskManager.rmv(101); // Removes task 101 from the system.
# taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
# taskManager.execTop(); // return 5. Executes task 105 for User 5.
 

# Constraints:

# 1 <= tasks.length <= 105
# 0 <= userId <= 105
# 0 <= taskId <= 105
# 0 <= priority <= 109
# 0 <= newPriority <= 109
# At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
# The input is generated such that taskId will be valid.


import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_map = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                userId, curPriority = self.task_map[taskId]
                if -priority == curPriority:
                    del self.task_map[taskId]
                    return userId
        return -1
