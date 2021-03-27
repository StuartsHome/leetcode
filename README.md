# Standard Algorithms
## Permutations

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