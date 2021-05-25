# Leetcode 787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        
        def dfs():
            pass

        for i in flights:
            dfs()


Run = Solution()
Run.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)

dist = {}
prev = {}
def dijkstra(Graph, source):
    q = set()
    for v in Graph:
        dist[v] = float('inf')
        prev[v] = None
        q.add(v)
    dist[source] = 0

    while q:
        u = min(q)
        q.remove(u)

        for v in u:
            alt = dist[u] + len(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev