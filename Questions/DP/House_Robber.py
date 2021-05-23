# Leetcode 198. House Robber

"""
Recursive formula
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
"""

class Solution:
    def rob(self, nums):
        
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

        """
        dp approach
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]