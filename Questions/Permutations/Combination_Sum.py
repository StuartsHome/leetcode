# Leetcode 39. Combination Sum

class Solution:
    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return []
        candidates.sort()
        result = []
        def dfs(ind, path, counter):
            if counter > target:
                return
            if counter == target:
                result.append(path)
            for i in range(ind, len(candidates)):
                dfs(i, [candidates[i]] + path, counter + candidates[i])
        dfs(0, [], 0)
        return result

run = Solution()
run.combinationSum([2,3,6,7], 7)