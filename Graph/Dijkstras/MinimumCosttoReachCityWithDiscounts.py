# A series of highways connect n cities numbered from 0 to n - 1.
# You are given a 2D integer array highways where highways[i] = [city1i, city2i, tolli]
# indicates that there is a highway connecting city1i and city2i, and you can travel in both directions.
#
# You are also given an integer discounts, representing how many discounts you can use.
# Each discount can be used on at most one highway, and reduces that highway's toll to tolli // 2.
#
# Return the minimum total cost to travel from city 0 to city n - 1.
# If it is not possible to reach city n - 1, return -1.
#
# ex:-
# n = 5
# highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]
# discounts = 1
# O/P -> 9
#
# Explanation:
# One optimal path is:
# 0 -> 1 -> 2 -> 3 -> 4
# Cost = 4 + 3 + 3 + 2 = 12
# Use the discount on highway [0,1] with toll 4, so it becomes 4 // 2 = 2
# Total cost = 2 + 3 + 3 + 2 = 10

# Idea:
# - Treat each state as (city, discounts_left).
# - Use Dijkstra's algorithm on this expanded state space.
# - From any state (city, k):
#   1. Move to a neighbor without using a discount.
#   2. Move to a neighbor using one discount, if k > 0.
# - Maintain dp[city][k] = minimum cost to reach that city with k discounts remaining.
# - The answer is the minimum value among all dp[n - 1][k].

from collections import defaultdict
import heapq
def minimumCost(n,highways,discount):
    dp = [[float('inf')]*(discount+1) for _ in range(n)]
    graph=defaultdict(list)
    for i in range(len(dp[0])):
        dp[0][i]=0
    for u,v,w in highways:
        graph[u].append((v,w))
        graph[v].append((u,w))
    heap=[(0,0,discount)]
    while len(heap):
        curr_dist,curr_node,k_remaining=heapq.heappop(heap)
        if curr_dist> dp[curr_node][k_remaining]:
            continue
        for nei,weight in graph[curr_node]:
            if curr_dist+weight < dp[nei][k_remaining]:
                dp[nei][k_remaining]=curr_dist+weight
                heapq.heappush(heap,(dp[nei][k_remaining],nei,k_remaining))
            if k_remaining and curr_dist+int(weight/2) < dp[nei][k_remaining-1]:
                dp[nei][k_remaining-1]=curr_dist+int(weight/2)
                heapq.heappush(heap,(dp[nei][k_remaining-1],nei,k_remaining-1))
    return min(dp[n-1]) if min(dp[n-1])!= float('inf') else -1

print(minimumCost(5,[[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]],1)) #O/P -> 9
print(minimumCost(4,[[0,1,3],[2,3,2]],0)) #O/P -> -1
print(minimumCost(4,[[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]],20)) #O/P -> 8




