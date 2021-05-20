# Leetcode 518. Coin Change 2 (Combinations)
# Unbounded knapsack - for each coin, we can use as many times as needed.
# Bottom-up dp:
# T: O(MN)
# S: O(N)
# Visualisation: https://leetcode.com/problems/coin-change-2/discuss/675089/Python-sol-by-DP-in-bottom-up-85%2B-w-Visualization

# Similar to Leetcode 377. Combination Sum IV
# Combination Sum IV -> Permutations


# This is Combinations, coin change 1 is Combinations also:
# 1. Permutations: -> Use each coin as many times as needed
# 2. Combinations: -> Use each coin once, but each coin may appear an infinite amount of times.


# Time: amount's recursive levels and n coins = O(n * amount)

class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for j in coins:
            for i in range(1, amount + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        # return dp[amount]
        print(dp)

Run = Solution()
Run.change(5, [1,2,5])


"""
Coin Change 2: [1,2,5] 5
1,1,2,2,3,4
CS IV: 
1,1,2,2,3,4

Coin Change 2: [1,2,5] 5
1,1,2,2,3,4
CS IV: 
1,1,2,2,3,4


"""

