


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0]) 
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = "#"
                    
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = 1
        
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != "#":
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        return obstacleGrid[rows-1][cols-1]


grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Run = Solution()
Run.uniquePathsWithObstacles(grid)
