# Standard Algorithms
## Permutations

### Standard Permutations (Any length)
- Returns permutations of any length
- input `Array`



- input `String`



### Standard Permutations of fixed length
#### Permuations - Backtrack (Same Technique)
Leetcode 46 - Permutations
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res 
Run = Solution()
Run.permute([1,1,2])
```
#### Permutations II - Backtrack - DFS
Leetcode 47 - Permutations II
```python
from collections import Counter
class Solution:
    def permuteUnique(self, nums):
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res 
Run = Solution()
Run.permuteUnique([1,1,2])
```
## Subsets - DFS
```python
class Solution:
    def subsets(self, nums):
        res = []
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
Run = Solution()
Run.subsets([1,2,3])
```
## Subsets II - DFS
```python
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
```
## Combination Sum - DFS
Notes: inside the dfs call, only loop variable called; not `ind`
```python
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
```




#### Outdated
- Return unique
```python
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 2:
        return [nums]

    memo = []
    for i, val in enumerate(nums):
        a = nums[:i] + nums[i+1:]
        for y in self.permuteUnique(a):
            if [val]+y in memo:
                break
            else:
                memo.append([val]+y) 
    return memo
```

- Backtrack
```python
class Solution:
    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        aa = res
        print(aa)
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
p1 = Solution()
p1.permute([1,2,3])
```

### Permutations of anagram
- Returns True if arg1 matches arg2
- Only returns anagrams of arg1 that matches it's length

```python
class Solution:
	def isAnagram(self, s, t):
		strs = list(s)
		if len(strs) <= 1:
			return [strs]
		memo = []
		for i, val in enumerate(strs):
			a = strs[:i] + strs[i+1:]

			for y in self.isAnagram(a, t):
				memo.append([val]+y)
				if t in memo:
					return True
		return memo

p1 = Solution()
p1.isAnagram("car", "rac")
```

### Permuations - No usable
The following doesn't play nicely with classes.
And only really works to print the values when encountered rather than
adding the result to a memo array.

```python
def perm(a, k=0):
   if k == len(a):
      print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm([1,2,3,4])
```