# Leetcode 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums):
        
        result = []
        nums.sort()
        def dfs(curr, path):
            result.append(path)
            for i in range(curr, len(nums)):
                if i > curr and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

Run = Solution()
Run.subsetsWithDup([1,2,2])