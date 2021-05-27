# Leetcode 1254. Number of Closed Islands
matrix = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
from collections import deque
class Solution:
    def closedIsland(self, grid):
        row, col = len(grid), len(grid[0])
        visited = set()
        q = deque()
        total = 0

        def bfs(r,c):
            grid[r][c] = 10
            q.append((r,c))
            visited.add((r,c))

            while q:
                rows, cols = q.popleft()
                directions = [[0,1], [1,0], [0,-1], [-1, 0]]
                for dr, dc, in directions:
                    if ((rows + dr) in range(row)
                    and (cols + dc) in range(col)
                    and (rows + dr, cols + dc) not in visited
                    and grid[rows + dr][cols + dc] == 0):
                        q.append((dr + rows, dc + cols))
                        visited.add((dr + rows, dc + cols))

        for r in [0, (row - 1)]:
            for c in range(col):
                if grid[r][c] == 0:
                    bfs(r,c)
        for r in range(row):
            for c in [0, (col - 1)]:
                if grid[r][c] == 0:
                    bfs(r,c)
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and grid[r][c] == 0:
                    total += 1
                    bfs(r,c)
        print(total)
Run = Solution()
Run.closedIsland(matrix)


"""
# Each island has to be surrounded by 1's
# Traverse the 0's
# if the 0 is in border return False for this island


m, n = len(grid), len(grid[0])
res = 0

def dfs(x, y):
    if x in (0, m-1) or y in (0, n-1):
        self.isIsland = False 
    for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
            grid[i][j] = -1 
            dfs(i, j)
            
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            self.isIsland = True
            dfs(i, j)
            res += self.isIsland
            
return res 
"""