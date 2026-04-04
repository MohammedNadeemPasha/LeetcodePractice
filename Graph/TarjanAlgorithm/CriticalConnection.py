# Given n servers numbered from 0 to n - 1 and a list of undirected connections where connections[i] = [ai, bi] represents a
# connection between server ai and server bi,return all critical connections in the network.
# A critical connection is an edge that, if removed, makes some servers unable to reach some other server.
# Return the answer in any order.
# ex:- n = 4, connections = [[0,1],[1,2],[2,0],[1,3]] ; O/P -> [[1,3]]
# n = 2, connections = [[0,1]] ; O/P -> [[0,1]]

# graph:-                        0       1       (example to illustrate where topo sort wouldn't work)
# 0 --- 1 --- 3                 / \     / \         (hence to find bridges we need tarjan's algo)
#  \   /                       2---3---4---5    (we start off by choosing a starting node and apply dfs)
#    2                          \ /     \ /     (keep track of disc and low and compare for every node) 
#                                6       7          (compare these values with its child node values)
#                            (If the network had disconnected nodes/disconnected graph then we would have to apply dfs on every node)
from collections import defaultdict
def criticalConnections(n, connections):
    low=[-1]*n
    disc=[-1]*n
    graph=defaultdict(list)
    result=[]
    for i in range(len(connections)):
        a,b=connections[i]
        graph[a].append(b)
        graph[b].append(a)
    def dfs(parent,node,time):
        disc[node]=time[0]
        low[node]=time[0]
        time[0]+=1
        for nei in graph[node]:
            if nei == parent:
                continue
            if disc[nei] == -1:
                dfs(node,nei,time)
                low[node]=min(low[node],low[nei])
                if low[nei]>disc[node]:
                    result.append([node,nei])
            else:
                low[node]=min(low[node],disc[nei]) 
    dfs(-1,0,[0])
    return result      

print(criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]])) # O/P -> [1,3]