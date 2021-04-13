# Leetcode 39. Combination Sum

class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        result = []
        def dfs(ind, path, curr):
            if curr > target:return
            if curr == target:
                result.append(path)
            for i in range(ind, len(candidates)):
                dfs(i, path+[candidates[i]], curr+candidates[i])
        dfs(0, [], 0)
        return result

Run = Solution()
Run.combinationSum([2,3,6,7], 7)