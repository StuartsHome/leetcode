# Subsequence


## Brute Force
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

## Recursion with Memoization
```python
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(prev_i, i):
            if i == len(nums): return 0
            if memo[prev_i + 1][i] >= 0:
                return memo[prev_i + 1][i]
            add, notAdd = 0, 0
            if prev_i < 0 or nums[i] > nums[prev_i]:
                add = 1 + helper(i, i + 1)
            notAdd = helper(prev_i, i + 1)
            memo[prev_i + 1][i] = max(add, notAdd)
            return memo[prev_i + 1][i]
			
        N = len(nums)
        memo = [[-1 for _ in range(N)] for _ in range(N)]        
        return helper(-1, 0)
```

## DP and Binary Search
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
LIS with not missing any numbers (i.e. consecutive numbers)