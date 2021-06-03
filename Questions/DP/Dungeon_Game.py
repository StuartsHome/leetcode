# Leetcode 174. Dungeon Game

# This is bottom-up DP, but starting from the bottom-right cell
# dp[i][j] is the minimum hp we need to reach the princess, if we start from point (i,j)
# Because we start from bottom-right, and check next row or next column
# we need a bottom dummy row and right dummy column to handle border cases
# The dummy rows and columns contain infinitives, except the neighbouring to the princess contain 1's.

# If at least one number is negative, this means we can survive with 1 hp
# If both are positive, we need to take minimum of them

# T: O(mn)
# S: O(mn), can be reduced O(min(m,n)) as we only look at neighbour cells, but code becomes more difficult to follow.
# S: can also be constant if we modify grid in place



# Link: https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained

grid = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1


        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[row][col] = max(min(dp[row + 1][col], dp[row][col+1]) - dungeon[row][col],1)
        # return dp[0][0]
        print(dp)
Run = Solution()
Run.calculateMinimumHP(grid)


