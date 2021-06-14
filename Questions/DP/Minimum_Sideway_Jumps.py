# Leetcode 1824. Minimum Sideway Jumps
# dp[i][j] means number of side jumps to reach i-th position and j-th lane.
# inf values in resulting dp array mean unreachable states.

class Solution:
    def minSideJumps(self, obstacles):
        dp = [[float("inf")] * 3 for _ in range(len(obstacles))]
        dp[0] = [1,0,1]             # We start in position in centre lane

        for i in range(1, len(obstacles)):
            for j in range(3):
                if obstacles[i] != j + 1:           # j + 1 is the action of moving to that stone so if obstacle == j + 1, we can't move to that stone so leave as infinity
                    dp[i][j] = dp[i - 1][j]         # if no obstacle, pull value from row before
            min_curr = min(dp[i])
            for j in range(3):                          # Simulates side jumps - this almost certainly updates the cell that was pulled from the last row but is infinity. So min(dp[i][j], min_curr + 1) will replace infinity with current minimum +1 for a side step
                if obstacles[i] != j + 1:               # If no obstacle moving to j + 1
                    dp[i][j] = min(dp[i][j], min_curr + 1)  # Take the min of infinity, or moving + 1 step
        # return min(dp[-1])
        print(dp)


Run = Solution()
Run.minSideJumps([0,1,2,3,0])


1   0   1
inf  0   1
2  inf  1
2  3  inf
