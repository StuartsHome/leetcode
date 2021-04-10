# Standard Algorithms
## Permutations

### Standard Permutations (Any length)
- Returns permutations of any length
- input `Array`



- input `String`



### Standard Permutations of fixed length
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

### Permuations Ints
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