# The Knapsack Problem (Woodcutting Problem)
## Introduction
The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

- Fractions: 
- No fractions: 0/1

## Problem Description - Knapsack
Rows are values x weights, Columns are capacity
Weights are in ascending order 
Considering the first item and figuring out the best possible capacity

### Coin Change
It's actually a complete backpack problem:
- capacity of the "backpack" is amount
- coins represents value of each item you can put into the "backpack"
- you can take 0 or many coins
- for each coin the cost is constant 1
- so the question is to find minimum cost to fill the "backpack"
```python
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

Run = Solution()
Run.coinChange([1,2,5], 11)
```

### Standard Knapsack
```python
class Solution:
    def knapsack(self, value, weight, capacity):
        ret_total = 0
        weight.insert(0,0)
        value.insert(0,0)
        N = len(weight) - 1
        
        def helper(n, total):
            if n == 0 or total == 0: return 0
            if weight[n] > total:
                return helper(n-1, total)
            else:
                #skip
                skip = helper(n - 1, total)
                #use
                use = value[n] + helper(n - 1, total - weight[n])
                result = max(skip, use)
            return result
        ret_total = helper(N, capacity)
        print(ret_total)
Run = Solution()
Run.knapsack([2,3,1,4], [3,4,6,5], 8)
```

### Memo Knapsack
To memoise:
1. Add memo of range(capacity) + 1, range(len(value)) + 1
2. Within helper method, add check if cell is != 0
3. Within helper at the end, before returning result, store in memo
```python
def Solution(value, weight, capacity):
    weight.insert(0, 0)
    value.insert(0,0)
    memo = [[0 for x in range(capacity + 1)] for a in range(len(value) + 1)]
    N = len(weight) - 1
    V = len(value) - 1
    def knapsack2(n, c):
        if memo[n][c] != 0: return memo[n][c]
        if n == 0 or c == 0: return 0
        elif weight[n] > c:
            return knapsack2(n-1, c)
        else:
            temp1 = knapsack2(n-1, c)
            temp2 = value[n] + knapsack2(n-1, c - weight[n])
            result = max(temp1, temp2)
        memo[n][c] = result
        return result
    aa = knapsack2(N, capacity)
    print(aa)
Solution([2,3,1,4], [3,4,6,5], 8)
```


## Problem Description - Zeroes and ones
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