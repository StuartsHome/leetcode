# Given weights and values of n items, put these items in a knapsack of capacity W 
# to get the maximum total value in the knapsack.


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