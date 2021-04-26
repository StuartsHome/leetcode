# Leetcode 62. Unique Paths

class Solution:
    def uniquePaths(self, m, n):
        dp = [[0]*n]*m

        dp[0][0] = 1

        for i in range(1,m):
            dp[i][0] = 1

        for j in range(1, n):
            dp[0][j] = 1

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m-1][n -1]

        print(dp)
Run = Solution()
Run.uniquePaths(3, 7)