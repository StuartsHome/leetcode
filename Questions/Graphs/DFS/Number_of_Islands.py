matrix = []
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c] == '1':
                grid[r][c] = '#'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            else:
                return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count
Run = Solution()
Run.numIslands(matrix)