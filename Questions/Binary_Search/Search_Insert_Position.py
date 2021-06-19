# Leetcode 35. Search Insert Position
# Classical binary search problem, where we need to return beg in the end, because we are looking for left place to insert our symbol.

# T: O(log n)
class Solution:
    def searchInsert(self, nums, target):
        
        upper, lower = len(nums), 0
        
        while lower < upper:
            ind = lower + (upper - lower) // 2
            val = nums[ind]
            if val >= target:
                upper = ind
            else:
                lower = ind + 1 # +1 because we're comparing current index w/ val, and if target > val we need to increase lower
        return lower
                

Run = Solution()
Run.searchInsert([1,3,5,6, 9, 10, 15, 20, 25], 26)