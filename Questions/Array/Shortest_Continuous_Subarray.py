# Leetcode 581. Shortest Unsorted Continuous Subarray

# T: O(n)
# S: O(1)

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


"""if len(nums) <2:
    return 0

prev = nums[0]
end = 0
# find the largest index not in place
for i in range(0, len(nums)):
    if nums[i] < prev:
        end = i
    else:
        prev = nums[i]

start = len(nums) - 1
prev = nums[start]
# find the smallest index not in place
for i in range(len(nums)-1, -1, -1):
    if prev < nums[i]:
        start = i
    else:
        prev = nums[i]
if end != 0:
    return end - start + 1
else: 
    return 0"""