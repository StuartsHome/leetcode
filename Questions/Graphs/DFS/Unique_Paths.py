# Leetcode 62. Unique Paths

class Solution:
    def uniquePaths(self, m, n):

        # dp = [[0] * n] * m]
        dp = [[0]*n]*m

        # for c in range(n):
        #     dp[0][c] = 1

        for r in [0, 0]:
            for c in range(n):
                dp[r][c] = 1

        for r in range(m):
            for c in [0]:
                dp[r][c] = 1


        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m-1][n -1]

        print(dp)
Run = Solution()
Run.uniquePaths(3, 7)