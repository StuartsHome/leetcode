# Leetcode 55. Jump Game

class Solution:
    def canJump(self, nums):
        curr_max = 0
        for i in range(len(nums)):
            if curr_max < i:
                return False
            if curr_max >= len(nums) - 1:
                return True
            curr_max = max(curr_max, i + nums[i])


Run = Solution()
Run.canJump([2,0])
([1])
([2,5,0,0])
([2,3,1,1,4])


        # result = 0
        # curr_max = nums[0]
        # total_max = 0
        # i = 0
        # # for i in range(1, len(nums)):
        # while True:
        #     if i >= len(nums):
        #         return False
        #     if i == len(nums) -1:
        #         return True
        #     if i >= curr_max:
        #         if nums[i] == 0 and i < len(nums):
        #             return False
        #         curr_max = nums[i]
        #     i += 1
