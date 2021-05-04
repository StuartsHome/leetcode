# Leetcode 665. Non-decreasing Array
"""
When count equals one, we check if we can modify nums[i] (the first one in the descending pair,
by decreasing it) or nums[i+1] (the second one in the descending pair, by increasing it),
if in both situations, we cannot, then we will also return False. 
"""


class Solution:
    def checkPossibility(self, nums):
        # Solution 1 - Intuitive
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i+2]<nums[i])):
                    return False
        return True

        # Solution 2 - Not intuitive
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)

Run = Solution()
Run.checkPossibility([3,4,2,3])
([4,2,1])
([4,2,3])