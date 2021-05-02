# Backtracking Solutions
Backtracking is a general algorithm for finding all (or some) solutions to problems, notably constraint satisfaction problems,\
that incrementally builds candidates to the solutions, and abandons a candidate ("bactracks") as soon as it determines that the\
candidate cannot possibly be completed to a valid solution.


### Subsets
```python
class Solution:
    def subsets(self, nums):
        
        result = []
        def dfs(ind, path):
            result.append(path)
            for i in range(ind, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result

Run = Solution()
Run.subsets([1,2,3])
```

### Subsets II
```python
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
```

### Combination Sum - Start from bottom
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
### Combination Sum III - Start from the top
All combinations of `k` that sum to `n`.
```python
class Solution:
    def combinationSum3(self, k, n):
        result = []        
        def dfs(curr, path, total):
            if total < 0 or curr < 0:
                return
            if curr == 0 and total == 0:
                result.append(path)
            if path:
                use = path[-1] + 1
            else:
                use = 1
            for i in range(use, 10):
                dfs(curr - 1, path + [i], total - i)
        dfs(k, [], n)
        return result
Run = Solution()
Run.combinationSum3(3, 7)
```
### Permutations
```python
class Solution:
    def permute(self, nums):
        result = []
        def dfs(ind, path):
            if not ind:
                result.append(path)
            
            for i in range(len(ind)):
                dfs(ind[:i]+ind[i+1:], path + [ind[i]])

        dfs(nums, [])
        print(result) 
        
Run = Solution()
Run.permute([1,2,3])
```
