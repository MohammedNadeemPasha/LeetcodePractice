# Problem:- we are given:
# - an undirected graph with n nodes
# - edgeList[i] = [u, v, dist] means an edge between u and v with weight dist
# - queries[j] = [p, q, limit] asks whether p and q are connected
#   using only edges with weight strictly less than limit
#
# Return a boolean array where answer[j] is True if such a path exists, otherwise False.
# ex:-
# n = 3, edgeList = [[0,1,2],[1,2,4],[0,2,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
# O/P -> [False, True]
#
# Idea:
# - Use offline sorting + Union-Find.
# - Sort all edges by weight.
# - Sort queries by limit, while keeping their original index.
# - For each query [p, q, limit]:
#   - union all edges with weight < limit
#   - then check whether p and q belong to the same component
# - Store the result at the query’s original index.

def distanceLimitedPathsExist(n, edgeList, queries):
    parent=list(range(n))
    result=[False]*len(queries)
    edgeList.sort(key=lambda x: x[2])
    sorted_queries=sorted([(q, i) for i, q in enumerate(queries)],key=lambda x: x[0][2])
    def findParent(x):
        if parent[x]!=x:
            parent[x]=findParent(parent[x])
        return parent[x]
    def union(x,y):
        rx=findParent(x)
        ry=findParent(y)
        if rx!=ry:
            parent[rx]=ry
    start=0
    for q,i in sorted_queries:
        u,v,w = q
        while start<len(edgeList) and edgeList[start][2]<w:
            union(edgeList[start][0],edgeList[start][1])
            start+=1
        result[i]= findParent(u)==findParent(v)
    return result

        
        