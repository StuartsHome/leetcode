# Leetcode 63. Unique Paths II
# Time Complexity - O(m * n)
# Space Complexity - O(1) - Utilizing the obstacleGrid as the DP array. Hence, no extra space.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        if obstacleGrid[0][0] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0]) 

        obstacleGrid[0][0] = 1

        for i in range(1,rows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
         # Filling the values for the first row        
        for j in range(1, cols):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
                else:
                    obstacleGrid[r][c] = 0
        return obstacleGrid[rows-1][cols-1]


grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Run = Solution()
Run.uniquePathsWithObstacles(grid)
