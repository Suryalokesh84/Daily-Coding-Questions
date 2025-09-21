# # code chef problem
# Self Defence Training
# After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

# The only condition for a woman to be eligible for the special training is that she must be between 
# 10
# 10 and 
# 60
# 60 years of age, inclusive of both 
# 10
# 10 and 
# 60
# 60.

# Given the ages of 
# N
# N women in his village, please help San Te find out how many of them are eligible for the special training.

# Input Format
# The first line of input contains a single integer 
# T
# T, denoting the number of test cases. The description of 
# T
# T test cases follows.
# The first line of each test case contains a single integer 
# N
# N, the number of women.
# The second line of each test case contains 
# N
# N space-separated integers 
# A
# 1
# ,
# A
# 2
# ,
# .
# .
# .
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,...,A 
# N
# ​
#  , the ages of the women.
# Output Format
# For each test case, output in a single line the number of women eligible for self-defence training.

# Constraints
# 1
# ≤
# T
# ≤
# 20
# 1≤T≤20
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# 1
# ≤
# A
# i
# ≤
# 100
# 1≤A 
# i
# ​
#  ≤100
# Sample 1:
# Input
# Output
# 3
# 3
# 15 23 65
# 3
# 15 62 16
# 2
# 35 9
# 2
# 2
# 1
# Explanation:
# Test Case 
# 1
# 1: Out of the women, only the 
# 1
# s
# t
# 1 
# st
#   and 
# 2
# n
# d
# 2 
# nd
#   women are eligible for the training because their ages lie in the interval 
# [
# 10
# ,
# 60
# ]
# [10,60]. Hence the answer is 2.

# Test Case 
# 2
# 2: Only the 
# 1
# s
# t
# 1 
# st
#   and 
# 3
# r
# d
# 3 
# rd
#   women are eligible for the training because their ages lie in the interval 
# [
# 10
# ,
# 60
# ]
# [10,60]. Hence the answer is again 2.

# Test Case 
# 3
# 3: Only the 
# 1
# s
# t
# 1 
# st
#   woman with age 
# 35
# 35 is eligible for the training. Hence the answer is 
# 1
# 1.


t = int(input())
for _ in range(t):
    n = int(input())
    ages = list(map(int, input().split()))
    count = 0
    for age in ages:
        if 10 <= age <= 60:
            count += 1
    print(count)



# explanation:
# The code reads the number of test cases and for each test case, it reads the number       
# =========================================================================
# leet code problem   



# 3508. Implement Router
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

# source: A unique identifier for the machine that generated the packet.
# destination: A unique identifier for the target machine.
# timestamp: The time at which the packet arrived at the router.
# Implement the Router class:

# Router(int memoryLimit): Initializes the Router object with a fixed memory limit.

# memoryLimit is the maximum number of packets the router can store at any given time.
# If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
# bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.

# A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
# Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
# int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.

# Remove the packet from storage.
# Return the packet as an array [source, destination, timestamp].
# If there are no packets to forward, return an empty array.
# int getCount(int destination, int startTime, int endTime):

# Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
# Note that queries for addPacket will be made in increasing order of timestamp.

 

# Example 1:

# Input:
# ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
# [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

# Output:
# [null, true, true, false, true, true, [2, 5, 90], true, 1]

# Explanation

# Router router = new Router(3); // Initialize Router with memoryLimit of 3.
# router.addPacket(1, 4, 90); // Packet is added. Return True.
# router.addPacket(2, 5, 90); // Packet is added. Return True.
# router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
# router.addPacket(3, 5, 95); // Packet is added. Return True
# router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
# router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
# router.addPacket(5, 2, 110); // Packet is added. Return True.
# router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.
# Example 2:

# Input:
# ["Router", "addPacket", "forwardPacket", "forwardPacket"]
# [[2], [7, 4, 90], [], []]

# Output:
# [null, true, [7, 4, 90], []]

# Explanation

# Router router = new Router(2); // Initialize Router with memoryLimit of 2.
# router.addPacket(7, 4, 90); // Return True.
# router.forwardPacket(); // Return [7, 4, 90].
# router.forwardPacket(); // There are no packets left, return [].
 

# Constraints:

# 2 <= memoryLimit <= 105
# 1 <= source, destination <= 2 * 105
# 1 <= timestamp <= 109
# 1 <= startTime <= endTime <= 109
# At most 105 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
# queries for addPacket will be made in increasing order of timestamp.






from collections import deque, defaultdict
from sortedcontainers import SortedList

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # Stores packets in FIFO order
        self.packet_set = set()  # To check duplicates: (source, destination, timestamp)
        self.dest_map = defaultdict(SortedList)  # destination -> SortedList of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False  # Duplicate

        # Remove oldest if memory is full
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_time))
            self.dest_map[old_dst].remove(old_time)

        # Add new packet
        self.queue.append((source, destination, timestamp))
        self.packet_set.add(key)
        self.dest_map[destination].add(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        src, dst, time = self.queue.popleft()
        self.packet_set.remove((src, dst, time))
        self.dest_map[dst].remove(time)
        return [src, dst, time]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map.get(destination, SortedList())
        left = timestamps.bisect_left(startTime)
        right = timestamps.bisect_right(endTime)
        return right - left
