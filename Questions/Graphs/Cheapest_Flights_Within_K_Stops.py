# Leetcode 787. Cheapest Flights Within K Stops
# No visited map
# This is because we need visited map to stop inifinite loops.
# Here, "K" limits the time we can visit a single node and stops infinite loop.


# We start from src and only got K+1 stops to use
# Each time, we choose the cheapest place to go.
# If the city we popout is dst, then the price must be the lowest.
# Since we always pick the lowest place to go

# If we still have stops left (stops>1), we put its neighbour to the
# priority queue. So the city in the priority queue must be within stops limit.

# Making the graph takes -> O(E)
# The size of priority queue is -> O(V), since we put all cities in it.
# For every pop, it is O(log V). 
# Total queue plus pop is O(V log V)

# T: O((V + E) log V)
# V is the number of cities within K stops

# Heap, the smallest element is always the root.
# Heapq, uses zero-based indexing
# Pop returns smallest item, not the largest

# [From, to, price]

import collections
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = {}

        for u in range(n):
            graph[u] = []

        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0,-K,src)]

        while heap:
            (cost,i,u) = heapq.heappop(heap)

            if u == dst:
                return cost

            for v,w in graph[u]:
                nc = cost + w

                if i <= 0:
                    heapq.heappush(heap, (nc,i+1,v))

        return -1   

        # graph = collections.defaultdict(list)
        # q = []

        # for start, dest, cost in flights:
        #     graph[start].append((cost, dest))

        # heapq.heappush(q, (0, K+1, src))
        # while q:
        #     price, stops, city = heapq.heappop(q)
            
        #     if city == dest:
        #         return price
        #     if stops > 0:
        #         for price_to_neigh, neig in graph[city]:
        #             heapq.heappush(q, (price + price_to_neigh, stops - 1, neig))

        # return -1
        
        # # Using visited default dict
        # adj, visited = defaultdict(dict), defaultdict(set) #visited[v] = {<steps we can reach city v with a shortest path>}
        # for s,e,w in flights:
        #     adj[s][e] = w # build a adjacent list
        # heap = [(0, K+1, src)] # (cost, limitation, city)
        # while heap:
        #     cost, step, u = heapq.heappop(heap)
        #     if step in visited[u]:
        #         continue
        #     visited[u].add(step)
        #     if u == dst:
        #         return cost
        #     if step > 0:
        #         step -= 1
        #         for v, w in adj[u].items():
        #             if step in visited[v]: # if we have visited city 'v' with 'step' steps ever, we don't need to process it again.  The better solution must have been processed in previous loops.
        #                 continue
        #             heapq.heappush(heap, (cost + w, step, v))
        # return -1


Run = Solution()
Run.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)

# dist = {}
# prev = {}
# def dijkstra(Graph, source):
#     q = set()
#     for v in Graph:
#         dist[v] = float('inf')
#         prev[v] = None
#         q.add(v)
#     dist[source] = 0

#     while q:
#         u = min(q)
#         q.remove(u)

#         for v in u:
#             alt = dist[u] + len(u, v)
#             if alt < dist[v]:
#                 dist[v] = alt
#                 prev[v] = u
#     return dist, prev


# TLE - but accepted in 2020
# graph = {}

# for u in range(n):
#     graph[u] = []

# for u,v,w in flights:
#     graph[u].append((v,w))

# heap = [(0,-K,src)]

# while heap:
#     (cost,i,u) = heapq.heappop(heap)

#     if u == dst:
#         return cost

#     for v,w in graph[u]:
#         nc = cost + w

#         if i <= 0:
#             heapq.heappush(heap, (nc,i+1,v))

# return -1   