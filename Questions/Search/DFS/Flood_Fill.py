# Leetcode 733. Flood Fill
from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        row, col = len(image), len(image[0])
        q = deque()
        visited = set()
        
        def dfs(r, c, val, newColor):
            image[r][c] = newColor
            q.append((r,c))
            visited.add((r,c))

            while q:
                rows, cols = q.pop()
                directions = [[0,1], [0,-1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    if ((dr + rows) in range(row) and
                    (dc + cols) in range(col) and image[dr + rows][dc + cols] == val
                    and ((dr + rows, dc + cols) not in visited)):
                        image[dr + rows][dc + cols] = newColor
                        visited.add((dr + rows, dc + cols))
                        q.append((dr + rows, dc + cols))

        for r in range(row):
            for c in range(col):
                #print(r,c)
                if (r,c) == (sr,sc):
                    #print("match")
                    val = image[r][c]
                    dfs(r,c, val, newColor)
        return image


Run = Solution()
Run.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2)

