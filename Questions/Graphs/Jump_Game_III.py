# Leetcode 1306. Jump Game III
# BFS - T&S: O(n)
from collections import deque
class Solution:
    def canReach(self, arr, start):
        # BFS
        N = len(arr)
        q = deque()
        visited = set()
        
        def bfs():
            q.append(start)
            visited.add(start)
            while q:
                ind = q.popleft()
                if arr[ind] == 0:
                    return True
                for x in (ind - arr[ind], ind + arr[ind]):
                    if x in range(N) and x not in visited:
                        visited.add(ind)
                        q.append(x)
            return False
        return bfs()

        # DFS
        """
        N = len(arr)
        stack = []
        visited = set()
        
        def dfs():
            # visited.add(start)
            stack.append(start)
            while stack:
                ind = stack.pop()
                if arr[ind] == 0:
                    return True
                visited.add(ind)
                cand1, cand2 = ind - arr[ind], ind + arr[ind]
                if cand1 >= 0 and cand1 not in visited:
                    stack.append(cand1)
                if cand2 < N and cand2 not in visited:
                    stack.append(cand2)
                # OR - But Slower
                for x in (ind - arr[ind], ind + arr[ind]):
                    if x in range(N) and x not in visited:
                        stack.append(x)
            return False
        return dfs()
        """

Run = Solution()
Run.canReach([4,2,3,0,3,1,2], 5)