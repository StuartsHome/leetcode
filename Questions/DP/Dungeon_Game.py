# Leetcode 174. Dungeon Game


grid = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for c in range(1, n):
            dungeon[0][c] = dungeon[0][c - 1] + dungeon[0][c]
        for r in range(1, m):
            dungeon[r][0] = dungeon[r - 1][0] + dungeon[r][0]

        for row in range(1, m):
            for col in range(1, n):
                dungeon[row][col] = 

        print(dungeon)
Run = Solution()
Run.calculateMinimumHP(grid)


