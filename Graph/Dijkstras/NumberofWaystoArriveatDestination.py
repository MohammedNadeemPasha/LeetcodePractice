# You are given a city with n intersections numbered from 0 to n-1, connected by bi-directional roads.
# Each road is represented as roads[i] = [u, v, time], meaning it takes 'time' minutes to travel between u and v.
# It is guaranteed that every intersection is reachable from any other, and there is at most one road between any two intersections.
#
# Find the number of different ways to travel from intersection 0 to intersection n-1 in the shortest possible time.
# Since the answer can be large, return it modulo (10^9 + 7).
#
# ex:- n = 7
# roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# O/P -> 4

from collections import defaultdict
import heapq

def countPaths(n, roads):
    MOD=10**9 + 7
    dp = [float('inf')] * n
    dp[0]=0; graph=defaultdict(list)
    ways=[0]*n
    ways[0]=1
    heap=[(0,0)]
    for i in range(len(roads)):
        graph[roads[i][0]].append((roads[i][1],roads[i][2]))
        graph[roads[i][1]].append((roads[i][0],roads[i][2]))
        
    while len(heap):
        dist,curr_node=heapq.heappop(heap)
        if dist >dp[curr_node]:
            continue
        for neighbour in graph[curr_node]:
            new_dist=neighbour[1]+dist
            if new_dist < dp[neighbour[0]]:
                ways[neighbour[0]]=ways[curr_node]
                dp[neighbour[0]]=new_dist
                heapq.heappush(heap,(new_dist,neighbour[0]))
            elif new_dist == dp[neighbour[0]]:
                ways[neighbour[0]]=(ways[neighbour[0]] + ways[curr_node]) % MOD
                
    return ways[n-1]

print(countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) #O/P -> 4