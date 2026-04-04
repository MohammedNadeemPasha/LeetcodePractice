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