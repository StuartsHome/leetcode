# Leetcode 797. All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(curr, path):
            if curr == len(graph) - 1:
                result.append(path)
            else:
                for i in graph[curr]: # for all edges at current node
                    dfs(i, path + [i])
        result = []
        dfs(0,[0])          # Tracking path, start with a path containing the source
        return result


Run = Solution()
Run.allPathsSourceTarget()