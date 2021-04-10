# The Knapsack Problem (Woodcutting Problem)
## Introduction
The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

- Fractions: 
- No fractions: 0/1

## Problem Description
You are given an array of binary strings `strs` and two integers `m` and `n`.
Return the size of the largest subset of `strs` such that there are at most `m` 0's and `n` 1's in the subset.
A set `x` is a subset of a set `y` if all elements of `x` are also elements of `y`.
## Knapsack Integers
### No Memo Dict
```python
def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def findMax(strs, i, m, n):
            counter = 0
            if i <= len(strs)-1:                
                if m > 0 or n > 0:
                    # use it or skip it
                    m1 = strs[i].count('0')
                    n1 = strs[i].count('1')
                    use = 0
                    
                    # skip it
                    skip = findMax(strs, i+1, m, n)
                    
                    # use it
                    if m1 <= m and n1 <= n:
                        use = findMax(strs, i+1, m-m1, n-n1) + 1
                    
                    # update counter
                    counter = max(use, skip)
                                
            return counter
        aa = findMax(strs, 0, m, n)
        return aa
Run = Solution()
Run.findMaxForm(["10","0001","111001","1","0"], 5, 3)
```
### With Memo Dict
```python
def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.memo = {}
        def findMax(strs, i, m, n):
            if i <= len(strs)-1:
                if (i, m, n) in self.memo:
                    return self.memo[(i,m,n)]
                
                if m > 0 or n > 0:
                    # use it or skip it
                    m1 = strs[i].count('0')
                    n1 = strs[i].count('1')
                    use = 0
                    
                    # skip it
                    skip = findMax(strs, i+1, m, n)
                    
                    # use it
                    if m1 <= m and n1 <= n:
                        use = findMax(strs, i+1, m-m1, n-n1) + 1
                    
                    # update counter
                    counter = max(use, skip)
                    self.memo[(i,m,n)] = counter
                    
                    return self.memo[(i,m,n)]
            
            return 0
            
        counter = findMax(strs, 0, m, n)
        return counter
```

### Allocating List of Size (length x m x n)
```python
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        length = len(strs)
        dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(length+1)]
                    
        for i in range(1, length+1):
            s = strs[i-1]
            m1 = s.count('0')
            n1 = s.count('1')
            
            for j in range(m+1):
                for k in range(n+1):
                    # this string can be used, so choose to use or skip
                    if j >= m1 and k >= n1:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-m1][k-n1]+1)
                    
                    # definitely cannot use this string
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        
        return dp[-1][-1][-1]
```
## Knapsack Strings