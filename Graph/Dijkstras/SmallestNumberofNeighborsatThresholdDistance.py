# You are given n cities numbered from 0 to n - 1 and a list of weighted bidirectional edges,
# where edges[i] = [fromi, toi, weighti] represents a road between two cities.
#
# You are also given an integer distanceThreshold.
#
# For each city, count how many other cities are reachable through some path whose total distance is less than or equal to 
# distanceThreshold.
#
# Return the city with the smallest number of reachable cities. If multiple cities have the same minimum count, return the city 
# with the greatest index.
# ex:-
# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distanceThreshold = 4
# O/P -> 3
#
# ex:-
# n = 5
# edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
# distanceThreshold = 2
# O/P -> 0
#
# Idea:
# - Build an adjacency list for the weighted graph.
# - Run Dijkstra from each city to find shortest distances to all other cities.
# - Count how many cities are reachable within distanceThreshold.
# - Track the city with the smallest reachable count.
# - If there is a tie, choose the city with the greater index.

from collections import defaultdict
import heapq
from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf')]*n for _ in range(n)]
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        for i in range(len(dist)):
            self.dijkstra(i,graph,dist,distanceThreshold)
        result=[-1,float('inf')]
        print(dist)
        for i in range(len(dist)):
            count=0
            for j in range(len(dist[0])):
                if dist[i][j] != float('inf'):
                    count+=1
            if count<result[1]:
                result=[i,count]
            elif count==result[1]:
                if result[0]<i:
                    result[0]=i
        return result[0]
    
    def dijkstra(self,node,graph,dist,distanceThreshold):
        min_dist=[float('inf')]*len(dist)
        min_dist[node]=0
        dist[node][node]=0
        heap=[(0,node,distanceThreshold)]
        while len(heap):
            curr_dist,curr_node,left_threshold=heapq.heappop(heap)
            for nei,weight in graph[curr_node]:
                if weight>left_threshold:
                    continue
                # if dist[nei][curr_node]!==float('inf'):
                #     min_dist[nei]=dist[nei][curr_node]
                #     dist[][]=min_dist[nei]
                if weight+curr_dist<min_dist[nei]:
                    min_dist[nei]=weight+curr_dist
                    dist[node][nei]=min_dist[nei]
                    dist[nei][node]=min_dist[nei]
                    heapq.heappush(heap,(min_dist[nei],nei,left_threshold-weight))

print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))  # O/P -> 3