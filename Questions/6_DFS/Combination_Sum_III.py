# Leetcode 216. Combination Sum III

class Solution:
    def combinationSum3(self, k, n):
        result = []
        
        def dfs(curr, path, target):
            if target < 0 or curr < 0: return
            if target == 0 and curr == 0:
                result.append(path)
            use = path[-1] + 1 if path else 1
            for i in range(use, 10):
                dfs(curr - 1, path + [i], target - i)
        
        dfs(k, [], n)
        return result
Run = Solution()
Run.combinationSum3(3, 7)