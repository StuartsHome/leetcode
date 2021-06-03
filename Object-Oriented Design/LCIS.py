class Solution:
    def findLengthOfLCIS(self, nums):
        small = nums[0]
        left = 0
        for i in range(len(nums)):
            if nums[i] < small:
                left = i
            else:
                small = nums[i]


        big = nums[-1]
        right = 0
        # for j in range(len(nums)-1, -1, -1):
        for j in reversed(range(len(nums))):
            if nums[j] > big:
                right = j
            else:
                big = nums[j]
            
        if left == right: return 0
        return left - right + 1

Run = Solution()
Run.findLengthOfLCIS([1,3,2,2,2])
([1,3,5,7])
([1,3,5,4,7])


# left = nums[0]
# for i in range(len(nums)):
#     if nums[i] < nums[i - 1]:
#         left = i


# big = nums[-1]
# right = 0
# # for j in range(len(nums)-1, -1, -1):
# for j in reversed(range(len(nums))):
#     if nums[j] > big:
#         right = j
#     else:
#         big = nums[j]
        
# if left == right: return 0
# return left - right + 1