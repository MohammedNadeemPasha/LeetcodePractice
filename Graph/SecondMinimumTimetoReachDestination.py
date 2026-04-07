# A city is represented as a bi-directional connected graph with n vertices, labeled from 1 to n.
# The graph is given as a 2D integer array edges, where each edges[i] = [ui, vi] represents
# a bi-directional edge between vertex ui and vertex vi.
# There is at most one edge between any pair of vertices, and no vertex has an edge to itself.
# The time taken to traverse any edge is time minutes.
#
# Each vertex has a traffic signal that alternates between green and red every change minutes.
# All signals switch color at the same time.
# You may enter a vertex at any time, but you can leave a vertex only when the signal is green.
# Also, you cannot wait at a vertex if the signal is green.
#
# The second minimum value is the smallest value strictly greater than the minimum value.
# ex:- second minimum of [2, 3, 4] = 3 ; second minimum of [2, 2, 4] = 4
#
# Given n, edges, time, and change, return the second minimum time required to travel
# from vertex 1 to vertex n.
#
# Notes:
# - You can visit any vertex any number of times, including 1 and n.
# - When the journey starts, all signals have just turned green.
#
# ex:-
# n = 5
# edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
# time = 3
# change = 5
# O/P -> 13
from collections import defaultdict,deque
def secondMinimum( n, edges, time, change):
    dp=[[float('inf')]*2 for _ in range(n)]
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q=deque()
    dp[0][0]=0
    q.append((1,0))
    while len(q):
        curr_node,curr_time=q.popleft()
        if curr_time != 0:
            curr_period=int(curr_time/change)
            if curr_period%2!=0:
                curr_time+=change-(curr_time%change)
        for nei in graph[curr_node]:
            if dp[nei-1][0] > curr_time+time:
                dp[nei-1][0] = curr_time+time
                q.append((nei,curr_time+time))
            elif dp[nei-1][0] < curr_time+time < dp[nei-1][1]:
                dp[nei-1][1] = curr_time+time
                q.append((nei,curr_time+time))
    return dp[n-1][1]

print(secondMinimum(5,[[1,2],[1,3],[1,4],[3,4],[4,5]],3,5)) #O/P -> 13