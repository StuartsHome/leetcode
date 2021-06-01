# Leetcode 746. Min Cost Climbing Stairs

# Solution 1 is:
# T: O(N)
# S: O(N)

# Space can be reduced to O(1) Solution 2

class Solution:
    def minCostClimbingStairs(self, cost):
        # Solution 1. DP Bottom Up
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * len(cost) 
        dp[0] = cost[0]
        dp[1] = cost[1]
            
        for i in range(2, len(cost)):
            temp = min(cost[i - 2], cost[i - 1])  
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])        

        print(dp)

        # Solution 2. 
        N = len(cost)
        if N == 0 or N == 1:
            return 0
        first, second = cost[0], cost[1]
        for i in range(2, N):
            first, second = second, cost[i] + min(first, second)
        return min(first, second)

Run = Solution()
Run.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])


([10, 15, 20])