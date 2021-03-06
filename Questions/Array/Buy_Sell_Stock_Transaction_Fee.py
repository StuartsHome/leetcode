# Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash



Run = Solution()
Run.maxProfit([1,3,2,8,4,9], 2)