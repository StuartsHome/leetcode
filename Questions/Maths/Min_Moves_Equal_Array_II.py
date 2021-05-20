# Leetcode 462. Minimum Moves to Equal Array Elements II
# Find the median:
# - we can effectively reduce the problem size from n to n-2 by discarding min and max points.
#   Do you see it? That is the definition of median, isn't it?
# Not mean because:
# - mean is where
# sum of distances to smaller elements = sum of distances to larger elements.
# So net number of moves
# = 2 * (either sum of distances to lower or larger elements)

# Good explanation: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94932/Why-median-is-better-than-average


# Use sorted instead of sort:
# 1. sorted returns a sorted list and can be used on any iterable
# 2. sort modifies the list in place, and returns None. It's usually less convenient than sorted()


# 1. As we want the min. steps to make the array equal, it would be better, if we start with an element that is at minimum distance from all the numbers combined.
# 2. So for that we sort the array and get the median of the array.
# 3. Now we sum the difference between the median and individual element in the sorted array.
# 4. The sum is our final answer.

class Solution:
    def minMoves2(self, nums):
        N = sorted(nums)
        mid = len(nums) //2
        val = N[mid]
        count = 0
        for num in N:
            count += abs(num - val)
        return int(count)


Run = Solution()
Run.minMoves2([1,2,3])