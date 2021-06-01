# Leetcode 934. Shortest Bridge

# Find the first island with 2 for loops
# Use DFS to find all connected 1 locations.
# There are only two islands so we only need to find the first one 
# Add all the first island 1 coordinates to queue and change 1's to 2's
# Run BFS on coordinates and increment steps for each level
# When BFS finds the first 1, return steps


# grid = [[0,1],[1,0]]
grid = [[0,1,0],[0,0,0],[0,0,1]]
from collections import deque
class Solution:
    def shortestBridge(self, grid):
        m, n = len(grid), len(grid[0])
        self.result = []
        visited = set()
        q = deque()
        
        def dfs(r, c):
            if r in range(m) and c in range(n) and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            else:
                return
        
        # Two while loops in bfs because we want to increment steps when all items of that level in queue have been used
        # If one while loop, we would increment steps after one item of that level used.
        def bfs():
            steps = 0
            while q:
                size = len(q)
                while size:
                    size -= 1
                    rows, cols = q.popleft()
                    
                    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                    for dr, dc in directions:
                        if ((dr + rows) in range(m) 
                            and (dc + cols) in range(n)
                            and grid[dr + rows][dc + cols] != 2):
                            if grid[dr + rows][dc + cols] == 1:
                                return steps
                            grid[dr + rows][dc + cols] = 2
                            q.append((dr + rows, dc + cols))
                steps += 1
            return steps
        # First - DFS 
        found = False
        total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break
            if found:
                break
        total = bfs()
                
        return total if total else -1

Run = Solution()
Run.shortestBridge(grid)