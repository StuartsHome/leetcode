# Leetcode 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
Run = Solution()
Run.subsetsWithDup([1,2,2])