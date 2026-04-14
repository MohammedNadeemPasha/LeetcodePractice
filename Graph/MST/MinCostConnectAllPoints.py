# You are given an array points where each point is represented as [x, y].
# The cost to connect two points is their Manhattan distance: - |x1 - x2| + |y1 - y2|
# Return the minimum cost needed to connect all points.
#
# All points are considered connected if there is exactly one simple path between any two points.
# That means we want to build a Minimum Spanning Tree (MST).
#
# ex:-
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# O/P -> 20
#
# Idea:
# - Treat each point as a node in a graph.
# - The weight between any two nodes is their Manhattan distance.
# - We need the minimum total cost to connect all nodes without cycles.
# - This is a classic Minimum Spanning Tree problem.
# - Use Prim’s algorithm:
#   - Start from one point
#   - Repeatedly add the cheapest edge that connects a new point
#   - Keep going until all points are included
# - The sum of all chosen edge costs is the answer.
#================IMP===================
#Prims only works when the graph is WEIGHTED,UNDIRECTED,NON-CYCLE,CONNECTED
# - if the graph is disconnected, Prim’s gives a Minimum Spanning Forest instead
# - The goal is to connect all nodes with minimum total cost while avoiding cycles
# - Prim’s algorithm always produces an MST
# - If the MST is unique, then the final structure will be the same regardless of which starting node we choose
# - However, the path/order of picking edges can be different depending on the start node
# - If multiple MSTs exist then starting from different nodes may produce different valid MSTs

from collections import defaultdict
import heapq
def minCostConnectPoints(points) :
    graph=defaultdict(list)
    minimum=float('inf')
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            graph[i].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),j))
            graph[j].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i))
    return findMST(i,graph)
def findMST(node,graph):
    heap=[(0,node)]
    visited=set()
    result_dist=0
    while len(heap):
        curr_dist,curr_node=heapq.heappop(heap)
        if curr_node in visited:
            continue
        visited.add(curr_node)
        result_dist+=curr_dist
        for w,nei in graph[curr_node]:
            if nei not in visited:
                heapq.heappush(heap,(w,nei))
    return result_dist
print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # O/P -> 20
        