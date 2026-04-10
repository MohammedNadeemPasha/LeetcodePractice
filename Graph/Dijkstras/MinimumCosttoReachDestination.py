# There are n cities numbered from 0 to n - 1, connected by bidirectional roads. Each road is represented as
# [x, y, time], meaning you can travel between city x and city y in 'time' minutes. There may be multiple roads
# between the same two cities, but no road connects a city to itself.
#
# Each city has a passing fee, given in the array passingFees, where passingFees[i] is the cost to pass through
# city i. You start at city 0 and want to reach city n - 1 in maxTime minutes or less.
#
# The total cost of a journey is the sum of the passing fees of every city visited, including the starting city
# and the destination city.
#
# Return the minimum cost needed to travel from city 0 to city n - 1 within maxTime minutes. If it is not possible, return -1.
#
# ex:- maxTime = 30,edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3] O/P -> 11
#
# Graph representation:
# 0 --10-- 1 --10-- 2 --10-- 5
#  \                           /
#   1                         15
#    \                       /
#     3 ------10------ 4 ----

#=============== MY SCUFFED SOLUTION =======================

from collections import defaultdict
import heapq

def minCost(maxTime, edges, passingFees) :
    cost=defaultdict(list)
    graph=defaultdict(list)
    count=-1
    for u,v,w in edges:
        if u not in graph:
            cost[u]=[float('inf')]*2
            graph[u]=[(v,w)]
            count+=1
        else:
            graph[u].append((v,w))
        if v not in graph:
            cost[v]=[float('inf')]*2
            graph[v]=[(u,w)]
            count+=1
        else:
            graph[v].append((u,w))
    cost[0]=[passingFees[0],0]
    heap=[(passingFees[0],0,0)]
    while len(heap):
        fees,time,node=heapq.heappop(heap)
        for nei,weight in graph[node]:
            if fees+passingFees[nei]< cost[nei][0] and time+weight <= maxTime:
                cost[nei][0]=fees+passingFees[nei]
                if time+weight < cost[nei][1]:
                    cost[nei][1] = time+weight
                heapq.heappush(heap,(cost[nei][0],time+weight,nei))
            elif time+weight<cost[nei][1]:
                cost[nei][1] = time+weight
                heapq.heappush(heap,(fees+passingFees[nei],cost[nei][1],nei))
    return cost[count][0] if cost[count][0]!=float('inf') and cost[count][1]<= maxTime else -1

print(minCost(30,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3])) # O/P -> 11


#============== Proper Formatted Solution ==================

def minCost( maxTime, edges, passingFees) :
        n = len(passingFees)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # min_time[node] = smallest time we've seen for this node
        # min_cost[node] = smallest cost we've seen for this node
        min_time = [float('inf')] * n
        min_cost = [float('inf')] * n

        heap = [(passingFees[0], 0, 0)]  # (cost, time, node)
        min_time[0] = 0
        min_cost[0] = passingFees[0]

        while heap:
            cost, time, node = heapq.heappop(heap)

            if node == n - 1:
                return cost

            for nei, travel in graph[node]:
                new_time = time + travel
                if new_time > maxTime:
                    continue

                new_cost = cost + passingFees[nei]

                # keep a state if it improves either cost or time
                if new_cost < min_cost[nei] or new_time < min_time[nei]:
                    min_cost[nei] = min(min_cost[nei], new_cost)
                    min_time[nei] = min(min_time[nei], new_time)
                    heapq.heappush(heap, (new_cost, new_time, nei))

        return -1