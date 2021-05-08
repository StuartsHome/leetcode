# Leetcode 583. Delete Operations for Two Strings
# Similar to Longest Common Subsequence

class Solution:
    def minDistance(self, word1, word2):

        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return m+ n - 2 * dp[m][n]

Run = Solution()
Run.minDistance("sea", "eat")
("leetcode", "etco")
