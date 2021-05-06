# Leetcode 55. Jump Game

class Solution:
    def canJump(self, nums):
        # Similar to Jump Game II
        curr_max = 0
        for i in range(len(nums)):
            if curr_max < i:
                return False
            if curr_max >= len(nums) - 1:
                return True
            curr_max = max(curr_max, i + nums[i])

        #Reverse
        curr_max = len(nums) - 1                # Iterate backwards from second to last item until the first item
        for i in range(len(nums)-2, -1, -1):    # If this index has jump count which can reach to or beyond the last position
            if i + nums[i] >= curr_max:          # We just need to reach this new index
                curr_max = i
        return curr_max == 0

        # DP
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        
        for i in range(1, N - 1):
            if dp[i - 1] < i:
                return False
            dp[i] = max(i + nums[i], dp[i - 1])
            if dp[i] >= N - 1:
                return True
        return dp[N - 2] >= N - 1

Run = Solution()
Run.canJump([2,3,1,1,4])
([2,0])
([1])
([2,5,0,0])

