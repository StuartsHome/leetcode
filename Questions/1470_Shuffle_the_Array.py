
# Leetcode 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums, n):
        results = []
        
        i, j = 0, n
        while i < n * 2 and j < n * 2:
            results.append(nums[i])
            results.append(nums[j])
            i += 1
            j += 1
        return results
                
Run = Solution()
Run.shuffle([2,5,1,3,4,7], 3)

([1,2,3,4,4,3,2,1], 4)