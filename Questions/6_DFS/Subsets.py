# Leetcode 78. Subsets

class Solution:
    def subsets(self, nums):
        
        result = []
        def dfs(ind, path):
            result.append(path)
            for i in range(ind, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result

        """        
        result = [[]]
        for i in range(len(nums)):
            result += [x + [nums[i]] for x in result]
        return result
        """

Run = Solution()
Run.subsets([1,2,3])