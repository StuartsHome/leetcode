# Leetcode 53. Maximum Subarray
# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums):

        # current_sum = best_sum = nums[0]
        # for x in nums[1:]:
        #     current_sum = max(x, current_sum + x)
        #     best_sum = max(best_sum, current_sum)
        # return best_sum

        # Modify original array for DP
        """
        total = []
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
        """

        # DP
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] , dp[i-1] + nums[i] )   # Previous number plus current number
        return max(dp)


Run = Solution()
Run.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])