# Leetcode 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums, k):
        N = len(nums)
        j = curr = 0
        for ind, val in enumerate(nums):
            if val == 0:
                k -= 1

            if k < 0:
                if nums[j] == 0:
                    k += 1
                j += 1
        return ind - j + 1

        
        # for ind, val in enumerate(nums):
        #     curr += 1
        #     if val == 0:
        #         ks += 1
        #     if ks > k:
        #         curr -= nums[j]
        #         if nums[j] == 0:
        #             ks -= 1
        #         j += 1
        #     if ks == k:
        #         total = max(curr, minner)
        # return total

Run = Solution()
Run.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)