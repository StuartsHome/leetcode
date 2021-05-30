
# Start at top left
# Goal to reach bottom right
# only can move right or down
# avoid the obstacles "-1"
# Q: What is the max count for any path from top left to bottom right?

# grid = [
# [1, 1, 1, 1, 1],
# [1, 1, 1, 5, 1],
# [-1, -1, 1, -1, -1],
# [1, 1, -1, 1, 1]
# ]

# grid = [
# [1, 3, 1],
# [1, 5, 1],
# [4, 2, 1]
# ]

# grid = [[1,2,3],[4,5,6]]
grid = [[9,1,4,8]]

def hmm(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    
    if m == 1 or n == 1:
        return grid[m-1][n-1]

    for c in range(1, n):
        grid[0][c] = grid[0][c] + grid[0][c - 1]

    for r in range(1, m):
        grid[r][0] = grid[r][0] + grid[r - 1][0]

    for r in range(1, m):
        for c in range(1, n):
            # if r == 0 and c == 0:
            #     continue
            # else:
            aa = grid[r][c - 1] + grid[r][c]
            bb = grid[r- 1][c]+grid[r][c]
            grid[r][c] = min((grid[r][c - 1] + grid[r][c]), (grid[r- 1][c]+grid[r][c]))

    # return grid[m - 1][n - 1]
    
    print(grid)

hmm(grid)


    # m, n = len(grid), len(grid[0])

    # dp = [[0]*n]*m
    
    # for r in range(m):
    #     for c in range(n):
    #         if c == 0:
    #             dp[r][0] = grid[r][c]
    #         else:
    #             dp[r][c] = max(dp[r][c - 1], grid[r][c] + dp[r][c - 1])
    #         # dp[r][c] = max(grid[r][c] + grid[r - 1][c], grid[r][c] + grid[r][c - 1])
    #         # if grid[r][c] == -1:
    #         #     continue
    #         # else:
    # print(dp)