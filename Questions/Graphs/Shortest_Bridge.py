# Leetcode 934. Shortest Bridge

grid = [[0,1],[1,0]]
from collections import deque
class Solution:
    def shortestBridge(self, grid):

        m, n = len(grid), len(grid[0])
        self.result = []
        visited = set()
        q = deque()
        
        def dfs(r, c):
            pass
            
        def bfs(a, b):
            grid[r][c] = "#"
            q.append((a,b))
            while q:
                rows, cols = q.popleft()
                
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    if ((dr + rows) in range(m) 
                        and (dc + cols) in range(n)
                        and grid[dr + rows][dc + cols] != "#"
                        and grid[dr + rows][dc + cols] == 1):
                        
                        grid[dr + rows][dc + cols] = "#"
                        q.append((dr + rows, dc + cols))
            
        # First - BFS 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    bfs(r,c)
        return grid

Run = Solution()
Run.shortestBridge(grid)