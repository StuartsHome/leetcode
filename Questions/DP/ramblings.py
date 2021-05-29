
# Start at top left
# Goal to reach bottom right
# only can move right or down
# avoid the obstacles "-1"
# Q: What is the max count for any path from top left to bottom right?

grid = [
[1, 1, 1, 1, 1],
[1, 1, 1, 5, 1],
[-1, -1, 1, -1, -1],
[1, 1, -1, 1, 1]
]

def hmm(grid):
    m, n = len(grid), len(grid[0])

    dp = [[0]*n]*m
    
    for r in range(m):
        for c in range(n):
            if c == 0:
                dp[r][0] = grid[r][c]
            else:
                dp[r][c] = max(dp[r][c - 1], grid[r][c] + dp[r][c - 1])
            # dp[r][c] = max(grid[r][c] + grid[r - 1][c], grid[r][c] + grid[r][c - 1])
            # if grid[r][c] == -1:
            #     continue
            # else:
    print(dp)
hmm(grid)
