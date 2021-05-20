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

"""
# TLE
coins.sort(reverse = True)
N, self.res = len(coins), 2**31-1

def dfs(ind, path, total):
    if not path:
        self.res = min(self.res, total)
    for i in range(ind, N):
        if coins[i] <= path < coins[i] * (self.res - total):
            dfs(i, path - coins[i], total + 1)

for i in range(N):
    dfs(i, amount, 0)
return self.res if self.res < 2**31-1 else -1
"""