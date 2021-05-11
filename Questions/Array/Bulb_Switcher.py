# Leetcode 319. Bulb Switcher

class Solution:
    def bulbSwitch(self, n):

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(0, n + 1, i):
                dp[j] = 1 - dp[j]
        sum(dp[1:])
            
Run = Solution()
Run.bulbSwitch(10)