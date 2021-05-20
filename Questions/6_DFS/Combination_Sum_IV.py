# Leetcode 377. Combination Sum IV (This should be Permutations)
# Distinct integers, all combinations that add up to target, use item as many times as needed
# Length of input: 1 <= len(nums) <= 200

# T: O(n^2)
# S: O(N)

# if the number is in the outer loop, we are aiming to find how to create all targets using
# that number (no duplicates)
# If the target is in the outer loop, we are repeatedly trying to reuse that number on every iteration.

class Solution:
    def combinationSum4(self, nums, target):
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):          # F1      # offset from 1 to skip base case (first element)
            for j in nums:                      # F2      
                if i >= j:                    
                    dp[i] += dp[i - j]
        print(dp)

Run = Solution()
Run.combinationSum4([1,2,5], 5)
([1,2,3], 4)