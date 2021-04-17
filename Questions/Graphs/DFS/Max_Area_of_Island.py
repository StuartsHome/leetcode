# Leetcode 695. Max Area of Island
matrix = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                grid[r][c] = 0 # set to 0 so don't count again. 
                return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1
            return 0

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area


Run = Solution()
Run.maxAreaOfIslands(matrix)