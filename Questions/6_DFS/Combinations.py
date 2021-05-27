# Leetcode 77. Combinations
# Given two integers n and k, return all possible combinations of
# k numbers out of the range [1, n].

# T: O(2 ^ n)

class Solution:
    def combine(self, n, k):
        nums = [x for x in range(1, n + 1)]
        
        result = []
        def dfs(ind, path):
            if len(path) == k and path not in result:
                result.append(path)
                return
            for i in range(len(ind)):
                dfs(ind[i + 1:], path + [ind[i]])
        
        dfs(nums, [])
        return result
Run = Solution()
Run.combine(4,2)