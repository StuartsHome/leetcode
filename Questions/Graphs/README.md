# Info

## Topics
### DFS and BFS
- BFS for shortest path in an unweighted graph (just count shortest edges)
- DFS for shortest path in weighted graph
- DFS uses a stack, BFS uses a queue 
- BFS is difficult to do recursively without additional data structures because it uses a queue.


### DP (Dynamic Programming)
- DP = Recursion + Memoization + Guessing
- DP doesn't work on graphs with cyles. This is because the memo table hasn't finished computing when it's called again, resulting in an infinite loop.
- For (DAGS) cylic graphs it's ok
- Bottom-up algos do a topological sort of the dependency DAG (acyclic)

### Paths
BFS used for shortest path in unweighted graph

Find shortest path between Source `(s)` and target `(v)` for all `(v)`
- The memoized algorithm does a DFS, to do a Topological sort, to run one round of Bellman Ford


Find shortest path between Source `(s)` and target `(v)`
This is a single target shortest path

## DFS - Iterative
## DFS - Recursive
### Number of islands
```python
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
```
### Max area
- Return call in dfs have to be grouped into same call
```python
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
```
## BFS  - Iterative
## BFS - Recursive

# Closed Islands
```python
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
```
