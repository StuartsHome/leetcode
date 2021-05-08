# Leetcode 1143. Longest Common Subsequence
# 1. Recursion
    # Result is TLE, unless use @lru_cache(maxsize=None)
# 2. Recursion with Memoization
# 3. Bottom-up DP 

"""
In Python, there is an easy way to memoize a function call.
For example, if you call a function func(a,b) with same a and b over and over again,
the decorator @lru_cache from functools can memoize this function call with corresponding result so that you don't
need to compute over and over again. Internally, it is just creating a hashmap with function parameters as key and returned value as value
"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):

        m = len(text1)
        n = len(text2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def helper(i, j):
            if memo[i][j] < 0:
                if i == len(text1) or j == len(text2):
                    memo[i][j] = 0
                elif text1[i] == text2[j]:
                    memo[i][j] = 1 + helper(i + 1, j + 1)
                else:
                    memo[i][j] = max(helper(i + 1, j), helper(i, j + 1))
            return memo[i][j]
        return helper(0, 0)

Run = Solution()
Run.longestCommonSubsequence("ubmrapg", "ezupkr")
("ezupkr", "ubmrapg")

# Recursion - No memoization
""" 
@lru_cache(maxsize=None)
def helper(i, j):
    if i == len(text1) or j == len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 + helper(i + 1, j + 1)
    else:
        return max(helper(i + 1, j), helper(i, j + 1))

return helper(0, 0)
"""

# Bottom-up DP
"""
m = len(text1)
n = len(text2)
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for row in range(1, m + 1):
    for col in range(1, n + 1):
        if text1[row - 1] == text2[col - 1]:
            dp[row][col] = 1 + dp[row - 1][col - 1]
        else:
            dp[row][col] = max(dp[row][col- 1], dp[row -1][col])
return dp[m][n]
"""