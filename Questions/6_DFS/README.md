# Backtracking Solutions
Backtracking is a general algorithm for finding all (or some) solutions to problems, notably constraint satisfaction problems,\
that incrementally builds candidates to the solutions, and abandons a candidate ("bactracks") as soon as it determines that the\
candidate cannot possibly be completed to a valid solution.

### Combination Sum
Given an array of ints, and a target, return a list of all combinations where they sum to target
```python
class Solution:
    def combinationSum(self, candidates, target):
        if not candidates: return []
        result = []
        candidates.sort()
        def dfs(ind, path, curr):
            if curr > target:
                return
            if curr == target:
                result.append(path)
                return
            for i in range(ind, len(candidates)):
                dfs(i, path + [candidates[i]], curr + candidates[i])

        dfs(0, [], 0)
        return result

Run = Solution()
Run.combinationSum([2,3,6,7],7)
```
### Combination Sum III
All combinations of `k` that sum to `n`.
```python
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
```