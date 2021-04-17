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