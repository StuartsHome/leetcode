# Leetcode 532. K-diff Pairs in an Array
# T: O(n)
# S: O(n)

from collections import Counter
class Solution:
    def findPairs(self, nums, k):
        
        memo = Counter(nums)
        total = 0
        for i in memo:              # Key point to loop over memo, not array
            if k > 0 and i + k in memo:
                total += 1
            elif k == 0 and memo[i] > 1:
                total += 1
        return total

        # TLE - T: O(n^2)
        # nums = sorted(nums, reverse=True)
        # result = []
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] - nums[j]) == k:
        #             if (nums[i],nums[j]) not in result:
        #                 result.append((nums[i],nums[j]))
        # return len(result)
        # print(result)
    
Run = Solution()
Run.findPairs([3,1,4,1,5],2)

([1,3,1,5,4], 0)
([3,1,4,1,5], 2)