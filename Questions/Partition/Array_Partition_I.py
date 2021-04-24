# Leetcode 561. Array Partition I
# Time Complexity:
# - Sorting takes O(n log n), we iterate over the array only once.
# - Space O(log n)
class Solution:
    def arrayPairSum(self, nums):
        
        nums.sort()
        summer = 0
        for i in range(0, len(nums) - 1, 2):
            summer += nums[i]
        print(summer)

        """
        or
        nums.sort()
        return sum(nums[::2])
        """
Run = Solution()
Run.arrayPairSum([6,2,6,5,1,2])
([1,4,3,2])