# Leetcode 35. Search Insert Position
# Classical binary search problem, where we need to return beg in the end, because we are looking for left place to insert our symbol.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        upper, lower = len(nums), 0
        
        while lower < upper:
            ind = lower + (upper - lower) // 2
            val = nums[ind]
            if val >= target:
                upper = ind
            else:
                lower = ind + 1
        return lower
                