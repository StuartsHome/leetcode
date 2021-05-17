# Leetcode 1048. Longest String Chain
# DFS on strings

class Solution:
    def longestStrChain(self, words):
        memo = {word:None for word in words}

        def dfs(curr):
            if curr not in memo:
                return 0
            result = 0
            for i in range(len(curr)):
                result = max(result, 1 + dfs(curr[:i] + curr[i+1:]))
            memo[curr] = result
            return memo[curr]

        total = 0
        for word in memo:
            total = max(total, dfs(word))
        print(total)

Run = Solution()
Run.longestStrChain(["a","b","ba","bca","bda","bdca"])