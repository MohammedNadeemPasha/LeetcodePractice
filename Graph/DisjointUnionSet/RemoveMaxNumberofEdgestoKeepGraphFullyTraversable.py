# You are given an undirected graph with n nodes labeled from 1 to n.
# Each edge has one of three types:
# Type 1: Alice only
# Type 2: Bob only
# Type 3: both Alice and Bob
#
# Return the maximum number of edges that can be removed
# while still making the graph fully traversable for both Alice and Bob.
# Return -1 if impossible.
#
# ex:
# n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], O/P -> 2
#
# Idea:
# - Use two Union-Finds: one for Alice, one for Bob.
# - Process Type 3 edges first since both can use them.
# - If an edge connects nodes already connected, it is removable.
# - Then process Type 1 for Alice and Type 2 for Bob.
# - Finally, check both Alice and Bob have one connected component.
# - If not, return -1; otherwise return removable edge count.
def maxNumEdgesToRemove(n, edges):
    parent_Alice=list(range(n+1))
    parent_Bob=list(range(n+1))
    result=0
    def findAlice(x):
        if parent_Alice[x]!=x:
            parent_Alice[x]=findAlice(parent_Alice[x])
        return parent_Alice[x]
    def findBob(x):
        if parent_Bob[x]!=x:
            parent_Bob[x]=findBob(parent_Bob[x])
        return parent_Bob[x]
    def unionAlice(x,y):
        rootx=findAlice(x)
        rooty=findAlice(y)
        if rootx!=rooty:
            parent_Alice[rootx]=rooty
            return True
        else:
            return False
    def unionBob(x,y):
        rootx=findBob(x)
        rooty=findBob(y)
        if rootx!=rooty:
            parent_Bob[rootx]=rooty
            return True
        else:
            return False
    commonEdges=[]
    aliceEdges=[]
    bobEdges=[]
    for edge in edges:
        if edge[0]==1:
            aliceEdges.append(edge)
        elif edge[0]==2:
            bobEdges.append(edge)
        else:
            commonEdges.append(edge)
    for typ,u,v in commonEdges:
        alice_used = unionAlice(u, v)
        bob_used = unionBob(u, v)
        if not alice_used and not bob_used:
            result+=1
    for typ,u,v in aliceEdges:
        if not unionAlice(u,v):
            result+=1
    for typ,u,v in bobEdges:
        if not unionBob(u,v):
            result+=1
    prevAliceParent=findAlice(1)
    prevBobParent=findBob(1)
    for i in range(2,len(parent_Alice)):
        tempAlice=findAlice(i)
        tempBob=findBob(i)
        if tempAlice!=prevAliceParent:
            return -1
        if tempBob!=prevBobParent:
            return -1
    return result

print(maxNumEdgesToRemove(4,[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])) #O/P ->2