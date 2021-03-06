# Subsequence

## Longest Continuous Increasing Subsequence
### Brute Force
```python
class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        result = []
        for i in range(len(nums)):
            counter = 1
            for j in range(i, len(nums)- 1):
                if nums[j + 1] > nums[j]:
                    counter += 1
                else:
                    break
            result.append(counter)
        return max(result)
```
### One Pass
```python
class Solution:
    def findLengthOfLCIS(self, nums):
        if nums == []:return 0
        if len(nums) <= 1:return 1
        count = 1
        max_count = 1
        for i in range(1,len(nums)):
            if i and nums[i-1] < nums[i]:
                count += 1
                if count > max_count:
                    max_count = count
            else: count = 1
        return max_count
```
### DP
```python
class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
```
## Longest Increasing Subsequence
### Brute Force - O(2^n)
```python
class Solution:
    def lengthOfLIS(self, nums):
        # TLE - Solution
        def helper(nums, prev, curpos):
            if curpos == len(nums):
                return 0
            taken = 0
            if nums[curpos] > prev:
                taken = 1 + helper(nums, nums[curpos], curpos + 1)
            nottaken = helper(nums, prev, curpos + 1)
            return max(taken, nottaken)
        return helper(nums, float('-inf'), 0)  
```

### Recursion with Memoization - O(n^2)
```python
class Solution:
    def lengthOfLIS(self, nums):
        def helper(prev_i, i):
            if i == len(nums): return 0
            if memo[prev_i + 1] >= 0:
                return memo[prev_i + 1]
            add, notAdd = 0, 0
            if prev_i < 0 or nums[i] > nums[prev_i]:
                add = 1 + helper(i, i + 1)
            notAdd = helper(prev_i, i + 1)
            memo[prev_i + 1] = max(add, notAdd)
            return memo[prev_i + 1]
			
        N = len(nums)
        memo = [-1 for _ in range(N)]       
        return helper(-1, 0)
```

### DP and Binary Search
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = l + (r - l) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[l] = num
            size = max(size, l + 1)
        return size
```

DP
Knapsack (woodcutting)
Longest increasing subsequence

To do
Brute force of both Knapsack and LIS
Memoization of both 