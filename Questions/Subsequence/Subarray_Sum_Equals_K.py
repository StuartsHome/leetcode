# Leetcode 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        total = [0] * (len(nums) + 1)
        for i in range(1, len(total)):
            total[i] = total[i - 1] + nums[i - 1]
        for j in range(len(nums)):
            for x in range(j + 1, len(nums) + 1):
                if total[x] - total[j] == k:
                    count += 1
        print(total, count)

        # TLE - O(N^3)
"""        result = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                if total + nums[j] == k:
                    total += nums[j]
                    result += 1             
                else:
                    total += nums[j]
        print(result)"""
            

Run = Solution()
Run.subarraySum([1,-1,0],0)
([1,2,3], 3)
([1,1,1], 2)