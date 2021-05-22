# Leetcode 847. Shortest Path Visiting All Nodes
# Undirected graph, shortest path visiting all nodes.

# BFS for shortest path undirected graph
import collections
class Solution:
    def shortestPathLength(self, graph):
        #

        # memo, final, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        # print(memo, final, q)
        
        N = len(graph)
        masks = [i*2 for i in range(N)]
        allVisited = (1 << N) - 1

Run = Solution()
Run.shortestPathLength([[1,2,3],[0],[0],[0]])


"""
# BFS
memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
while True:
    new = []
    for node, state in q:
        if state == final: return steps
        for v in graph[node]:
            if (state | 1 << v, v) not in memo:
                new.append((v, state | 1 << v))
                memo.add((state | 1 << v, v))
    q = new
    steps += 1
"""
