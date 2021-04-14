# Leetcode 322. Coin Change
"""
It's actually a complete backpack problem:
- capacity of the "backpack" is amount
- coins represents value of each item you can put into the "backpack"
- you can take 0 or many coins
- for each coin the cost is constant 1
- so the question is to find minimum cost to fill the "backpack"
"""
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

Run = Solution()
Run.coinChange([1,2,5], 11)
