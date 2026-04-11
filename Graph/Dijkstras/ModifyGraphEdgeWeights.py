# You are given an undirected weighted connected graph with n nodes labeled from 0 to n - 1, and an integer array edges 
# where edges[i] = [ai, bi, wi] means there is an edge between nodes ai and bi with weight wi.
# Some edges have a weight of -1, while others already have a positive weight.
# Your task is to replace every edge with weight -1 with some positive integer in the range [1, 2 * 10^9] so that the 
# shortest distance from source to destination becomes exactly target.
#
# You are not allowed to change edges that already have a positive weight.
#
# Return all edges after modification in any order if it is possible to make the shortest path equal to target. Otherwise, 
# return an empty array.
# ex:-
# n = 5
# edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
# source = 0, destination = 1, target = 5
# O/P -> one valid modified version of edges, such as:
# [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
#
# ex:-
# n = 3
# edges = [[0,1,-1],[0,2,5]]
# source = 0, destination = 2, target = 6
# O/P -> []
#
# Idea:
# - Run Dijkstra first using only fixed positive edges.
# - If shortest path is already less than target, return [].
# - If shortest path is exactly target, set all -1 edges to a very large value.
# - Otherwise, try setting each -1 edge to 1 one by one.
# - As soon as shortest path becomes <= target, increase that edge by (target - current_dist).
# - Set all remaining -1 edges to a large value and return the result.
import heapq

def modifiedGraphEdges( n, edges,source, destination, target):
    INF = 2 * 10**9
    def dijkstra() -> int:
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            if w == -1:
                continue
            graph[a].append((b, w))
            graph[b].append((a, w))
        dist = [float('inf')] * n
        dist[source] = 0
        pq = [(0, source)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist[destination]
    dist = dijkstra()
    if dist < target:
        return []
    if dist == target:
        for e in edges:
            if e[2] == -1:
                e[2] = INF
        return edges
    for e in edges:
        if e[2] != -1:
            continue
        e[2] = 1
        dist = dijkstra()
        if dist <= target:
            e[2] += target - dist
            for rest in edges:
                if rest[2] == -1:
                    rest[2] = INF
            return edges
    return []

print(modifiedGraphEdges(5,[[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]],0,1,5)) #O/P ->[[4, 1, 1], [2, 0, 1], [0, 3, 1], [4, 3, 3]]