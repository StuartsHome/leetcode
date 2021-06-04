# Leetcode 70. Climbing Stairs


class Solution:
    def climbStairs(self, n):
        

        # Recursion w/ memoization
        # T: O(n), S: O(n)
        result = []
        memo = {}
        def dfs(ind, path):
            if ind in memo:
                return memo[ind]
            if ind > n:
                return 0
            if ind == n:
                return 1
            else:
                memo[ind] = dfs(ind + 1, path + [1]) + dfs(ind + 2, path + [2])
                return memo[ind]
        return dfs(0, [])

        # This works but TLE - T: O(2^n), S: O(n)
        # For every index you 
        result = []
        def dfs(ind, path):
            if sum(path) > n:
                return
            if sum(path) == n:
                result.append(path)
            else:
                dfs(ind + 1, path + [1])
                dfs(ind + 2, path + [2])
        dfs(1, [])
        return len(result)

            
        # DP
        # T: O(n), S: O(n)
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


Run = Solution()
Run.climbStairs(5)

"""
class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
            return( memo[n]  )
            """