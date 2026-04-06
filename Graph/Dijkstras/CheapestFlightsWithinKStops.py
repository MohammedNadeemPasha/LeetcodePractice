# There are n cities connected by flights. You are given flights where flights[i] = [fromi, toi, pricei]
# means there is a flight from city fromi to city toi with cost pricei.
# You are also given src, dst, and k. Return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.
# ex:- n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# O/P -> 700

import heapq                                               #  [ [inf, inf, inf, ...],
from collections import defaultdict                        #  [inf, inf, inf, ...],
from typing import List                                    #     ...]

def findCheapestPrice(n, flights, src, dst, k) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    best = [[float('inf')] * (k + 2) for _ in range(n)]
    best[src][k + 1] = 0
    heap = [(0, src, k + 1)]  
    while heap:
        cost, node, stops_left = heapq.heappop(heap)
        if node == dst:
            return cost
        if stops_left == 0:
            continue
        if cost > best[node][stops_left]:
            continue
        for nei, price in graph[node]:
            new_cost = cost + price
            if new_cost < best[nei][stops_left - 1]:
                best[nei][stops_left - 1] = new_cost
                heapq.heappush(heap, (new_cost, nei, stops_left - 1))
    return -1
print(findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1 )) #O/P -> 700