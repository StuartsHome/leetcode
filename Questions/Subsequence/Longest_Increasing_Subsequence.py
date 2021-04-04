# Leetcode 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums):
        # TLE - Solution
        def helper(nums, prev, curpos):
            if curpos == len(nums):
                return 0
            taken = 0
            if nums[curpos] > prev:
                taken = 1 + helper(nums, nums[curpos], curpos + 1)
            nottaken = helper(nums, prev, curpos + 1)
            return max(taken, nottaken)
        return helper(nums, float('-inf'), 0)        
        
        # TLE - Comments
        N = len(nums)
        def helper(last, i):
            if i == N: return 0
            add, notAdd = 0, 0
            if nums[i] > last:
                add = 1 + helper(nums[i], i + 1)
            notAdd = helper(last, i + 1)
            return max(add, notAdd)

        return helper(float('-inf'), 0)
            




Run = Solution()
Run.lengthOfLIS([0,1,0,3,2,3])
([10,9,2,5,3,7,101,18])