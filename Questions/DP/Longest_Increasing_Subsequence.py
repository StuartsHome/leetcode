# Leetcode 300. Longest Increasing Subsequence
# Naive DP - Time: O(N^2), Space: O(N)


class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        N = len(nums)
        dp = [1] * N
        
        for i in range(1, N):
            for j in range(i):                  # This for loop is to check from start of array to i
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
      
        return max(dp)

        """ Recursion with memoization
        # def helper(prev_i, i):
        #     if i == len(nums): return 0
        #     if memo[prev_i + 1] >= 0:
        #         return memo[prev_i + 1]
        #     add, notAdd = 0, 0
        #     if prev_i < 0 or nums[i] > nums[prev_i]:
        #         add = 1 + helper(i, i + 1)
        #     notAdd = helper(prev_i, i + 1)
        #     memo[prev_i + 1] = max(add, notAdd)
        #     return memo[prev_i + 1]
			
        # N = len(nums)
        # memo = [-1 for _ in range(N)]       
        # return helper(-1, 0)
        """
        # TLE - Solution
        # def helper(nums, prev, curpos):
        #     if curpos == len(nums):
        #         return 0
        #     taken = 0
        #     if nums[curpos] > prev:
        #         taken = 1 + helper(nums, nums[curpos], curpos + 1)
        #     nottaken = helper(nums, prev, curpos + 1)
        #     return max(taken, nottaken)
        # return helper(nums, float('-inf'), 0)        
        
        # TLE - Comments
        """
        N = len(nums)
        def helper(last, i):
            if i == N: return 0
            add, notAdd = 0, 0
            if nums[i] > last:
                add = 1 + helper(nums[i], i + 1)    # You only increment when curr is greater than last
            notAdd = helper(last, i + 1)               # if so, curr is the new last and + 1 to last
            return max(add, notAdd)     

        return helper(float('-inf'), 0)
        """
Run = Solution()
Run.lengthOfLIS([10,9,2,5,3,7,101,18])
([0,1,0,3,2,3])
