# You are given a directed graph with n nodes labeled from 0 to n - 1. Each edge is colored either red or blue.
# The graph may contain self-edges and parallel edges.
#
# You are given:
# - redEdges where redEdges[i] = [a, b] means there is a directed red edge from a to b
# - blueEdges where blueEdges[j] = [u, v] means there is a directed blue edge from u to v
#
# Return an array answer of length n, where answer[x] is the length of the shortest path
# from node 0 to node x such that the colors of edges along the path strictly alternate between red and blue.
#
# If there is no such path to node x, return -1 for that node.
# ex:-
# n = 3
# redEdges = [[0,1],[1,2]]
# blueEdges = []
# O/P -> [0,1,-1]
#
# ex:-
# n = 3
# redEdges = [[0,1]]
# blueEdges = [[1,2]]
# O/P -> [0,1,2]
# Explanation:
# - Reach node 1 using a red edge: 0 -> 1
# - Then take a blue edge: 1 -> 2
# - Colors alternate correctly, so node 2 is reached in 2 steps
#
# ============ MY SOLUTION IDEA =============
# Idea:
# - Build a graph storing neighbor and edge color.
# - Use a min-heap with states: (distance, node, previous_color).
# - Keep dp[node][color] as the shortest distance to reach that node
#   with the last edge having that color.
# - From each node, only move to edges whose color is different from previous_color.
# - Update dp and push into the heap whenever a shorter alternating path is found.
# - Final answer for each node is min(red-ending path, blue-ending path),
#   or -1 if neither exists.
#=======================================
#
# Idea:
# - Build two adjacency lists:
#   1. one for red edges
#   2. one for blue edges
# - Use BFS because all edges have equal weight 1
# - Treat each state as (node, last_color_used)
# - From a state where the last edge was red, the next edge must be blue
# - From a state where the last edge was blue, the next edge must be red
# - Start BFS from node 0 with both possibilities:
#   1. pretend the last edge was red, so next can be blue
#   2. pretend the last edge was blue, so next can be red
# - Keep visited[node][color] to avoid revisiting the same state
# - The shortest distance for each node is the first level in BFS where that node is reached

from collections import defaultdict
import heapq

def shortestAlternatingPaths(n, redEdges, blueEdges) :
    graph=defaultdict(list)
    answer=[-1]*n
    dp=[[float('inf')]*2 for _ in range(n)]
    for u,v in redEdges:
        graph[u].append((v,'r'))
    for u,v in blueEdges:
        graph[u].append((v,'b'))
    heap=[(0,0,'u')]
    dp[0][0]=0;dp[0][1]=0;answer[0]=0
    while len(heap):
        curr_dist,curr_node,prev_color=heapq.heappop(heap)
        for nei,next_color in graph[curr_node]:
            color=0
            if next_color == 'b':
                color=1
            if curr_dist+1<dp[nei][color] and next_color != prev_color:
                dp[nei][color]=curr_dist+1
                heapq.heappush(heap,(curr_dist+1,nei,next_color))
    for i in range(len(dp)):
        if min(dp[i])!=float('inf'):
            answer[i]=min(dp[i])
    return answer
print(shortestAlternatingPaths(3,[[0,1],[1,2]],[])) #O/P -> [0,1,-1]