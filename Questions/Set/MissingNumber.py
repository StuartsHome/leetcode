# Leetcode 268. Missing Number

class Solution:
    def missingNumber(self, nums):
        result = set([x for x in range(max(nums) + 1)])
        result_2 = set(nums) ^ result
        return list(result_2).pop() if result_2 else len(nums)


Run = Solution()
Run.missingNumber([3,0,1])

([0,1])



([9,6,4,2,3,5,7,0,1])

([3,0,1])