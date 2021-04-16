# Given weights and values of n items, put these items in a knapsack of capacity W 
# to get the maximum total value in the knapsack.

# Returning Optimum values - not the list of items
"""def Solution(value, weight, capacity):
    weight.insert(0, 0)
    value.insert(0,0)
    N = len(weight) - 1
    def knapsack2(n, c):
        if n == 0 or c == 0: return 0
        elif weight[n] > c:
            return knapsack2(n-1, c)
        else:
            temp1 = knapsack2(n-1, c)
            temp2 = value[n] + knapsack2(n-1, c - weight[n])
            result = max(temp1, temp2)
        return result
    aa = knapsack2(N, capacity)
    print(aa)
Solution([2,3,1,4], [3,4,6,5], 8)"""
#Solution([60,100,120], [10,20,30], 50)
#Solution([5,3,5,3,2], [1,2,4,2,5], 10)

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

# This is a bottom-up solution (not preferred)
"""
val = [50, 100, 150, 200]
weights = [8, 16, 32, 40]
capacity = 64

def knapsack(v, w, c):
    n = len(v)
    table = [[0 for x in range(c + 1)] for x in range(n + 1)]
    print(table)
    for i in range(n + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif w[i-1] <= j:
                table[i][j] = max(v[i-1]
                + table[i-1][j-w[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    print(table[n][c])
knapsack(val, weights, capacity)
"""