
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

        
        