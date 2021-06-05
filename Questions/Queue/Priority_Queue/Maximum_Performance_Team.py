# Leetcode 1383. Maximum Performance of a Team

# Priority Queue, greedy algorithm
# Greedy because we decompose a problem into a series of stages, and
# at each stage we make the locally optimal choice.

# Solution is derived from an enumeration process.
# At each step we build a locally optimal team by starting from a fixed engineer
# with the minimum efficiency on the team.
# At the end of the enumeration process, we select the maximum among the locally optimal
# solutions to obtain the globally optimal solution.

# The most complex step is the second step. 
# In the second step we have selected a member who will have the lowest
# efficieny in the team. Then we must determine how to construct the rest of the team.
# We must find all eligible candidates whose efficiencies are higher that the fixed member's efficiency
# Sorting the candidates in descending order based on efficiency
# We then iterate through the sorted candidates. For each candidate, we only
# need to consider the earlier candidates. Since the list is sorted, only
# the earlier candidates will have a higher efficiency than the current candidate.

# T: O(n (log n + log k))
# S: O(n + k) - n is size of candidates, k is capacity of queue

# 1. Build list of candidates from inputs, O(n)
# 2. Sort candidates, O(n log n)
# 3. Iterate through sorted candidates. At each iteration, we will perform at most two operations
# on the priority queue: one push and one pop.
# Each operation takes: O(log(k - 1)) time, where k - 1 is the capacity of the queue.
# The time complexity of this iteration will be: O(n log k)


import heapq
class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        
        modulo = 10 ** 9 + 7

        # Build tuples of (efficiency, speed)
        candidates = zip(efficiency, speed)
        # Sort the candidates in reverse by their efficiencies
        candidates = sorted(candidates, key=lambda x : x[0], reverse=True)

        speed_heap = [] # heap of speeds
        speed_sum, perf = 0, 0
        for curr_efficiency, curr_speed in candidates:
            # Maintain a heap for the fastest (k-1) speeds
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap) # pop and return smallest item from heap
            heapq.heappush(speed_heap, curr_speed)
        
            # Calculate the max performance with the current member
            # as the least efficient one in the team
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)

        return perf % modulo



Run = Solution()
Run.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)