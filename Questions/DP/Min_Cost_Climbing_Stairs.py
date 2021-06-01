# Leetcode 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * len(cost) 
        dp[0] = cost[0]
        dp[1] = cost[1]
            
        for i in range(2, len(cost)):
            temp = min(cost[i - 2], cost[i - 1])  
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])        

        print(dp)

Run = Solution()
Run.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])


([10, 15, 20])