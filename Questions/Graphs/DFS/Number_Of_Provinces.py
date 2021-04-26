# Leetcode 547. Number of Provinces
# Time Complexity: O(n^2). O(n^2) to construct the graph and O(n) to run DFS, so the total is O(n^2).

class Solution:
    def findCircleNum(self, isConnected):
        rows = len(isConnected)  #1
        visited = [False]*rows  #2
        count = 0  #3
        
        if not isConnected:  #4
            return 0  #5
        
        def dfs(r):  #6
            for cols in range(rows):  #7
                if isConnected[r][cols] == 1 and visited[cols] == False:  #8
                    visited[cols] = True  #9
                    dfs(cols)  #10
        
        
        for idx in range(rows): #11
            if visited[idx] == False: #12
                count += 1 #13
                visited[idx] = True #14
                dfs(idx) #15
        
        return count #16
Run = Solution()
Run.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])

([[1,1,0],[1,1,0],[0,0,1]])