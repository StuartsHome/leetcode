# Leetcode 322. Coin Change

class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        # copy_coins = sorted(coins, reverse=True)

        # copy_amount = amount
        # i = 0
        # total = 0
        # while copy_amount and i < len(copy_coins):
        #     while i < len(copy_coins) and copy_amount:
        #         if copy_coins[i] <= copy_amount:
        #             copy_amount -= copy_coins[i]
        #             total += 1
        #         else:
        #             i += 1
        # if copy_amount != 0:
        #     return -1
        # else:
        #     return total

Run = Solution()
Run.coinChange([1,2,5], 11)
([186,419,83,408], 6249)

([2],3)

