# Leetcode 674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthofLCIS(self, nums):
        # Clever DP
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
        """ SLOW
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        result = []
        for i in range(len(nums)):
            counter = 1
            for j in range(i, len(nums)- 1):
                if nums[j + 1] > nums[j]:
                    counter += 1
                else:
                    break
            result.append(counter)
        return max(result)
        """

        # N = len(nums)
        # result = []
        # def helper(last, i, add):
        #     if last == N: return 0
        #     if i < len(nums) and nums[i] > last:

        #     # #add = 1
        #     # if i < len(nums) and nums[i] > last:
        #     #     return helper(nums[i], i + 1, add + 1)
        #     # # if nums[i] > last:
        #     # #     add += 1
        #     # return add

        # for x in range(len(nums)):
        #     add = 1
        #     length = helper(x, x + 1, add)
        #     result.append(length)
        # print(result)


Run = Solution()
Run.findLengthofLCIS([1,3,5,4,2,3,4])

([2,2,2,2,2])


([1,2,5,8,0])


([1,3,5,4,7])

