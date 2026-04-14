# There are n cities numbered from 1 to n. Each connection is given as:
# - [city1, city2, cost] which means city1 and city2 can be connected with that cost.
#
# The connection is bidirectional: connecting city1 to city2 is the same as connecting city2 to city1
# Return the minimum total cost needed so that all cities are connected.
# If it is not possible to connect all cities, return -1.
#
# ex:-
# n = 3
# connections = [[1,2,5],[1,3,6],[2,3,1]]
# O/P -> 6
#
#================ Idea =======================
# - This is a Minimum Spanning Tree (MST) problem (Connecting all nodes with minimal cost)
# - Since connections are weighted and undirected, use Kruskal’s or Prim's algorithm
#  Kruskal + Union-Find makes it easy to detect disconnected graphs, and their roots
# where as in Prim's, we detect disconnection by checking whether all nodes were visited by the end of the traversal.
# Kruskal’s algorithm:
# - Sort all edges by cost
# - Pick the smallest edge each time
# - Only add it if it does not form a cycle
#
# To efficiently check cycles, use Union-Find (Disjoint Set Union):
# - Each city starts in its own set
# - If two cities belong to different sets, connect them
# - If they are already in the same set, skip that edge
#
# Why this works:
# - We always try the cheapest available connection first
# - We avoid cycles
# - This guarantees the minimum total cost spanning tree
#===================================================

def minimumCost(n,connections):
    parent=list(range(n+1))
    rank=[0]*(n+1)
    connections.sort(key=lambda x: x[2])
    min_weight=0
    for i in range(len(connections)):
        result=findmst(connections[i],parent,rank)
        if result:
            min_weight+=connections[i][2]
    def findParent(node):
        if parent[node]!= node:
            return  findParent(parent[node])
        return node
    initial=findParent(parent[1])
    print(parent)
    
    for i in range(2,len(parent)):
        if findParent(parent[i])!= initial:
            return -1
    return min_weight

    
def findmst(connection,parent,rank):
    def findParent(node):
        if parent[node]!= node:
            parent[node] = findParent(parent[node])
        return parent[node]
    
    rootX=findParent(connection[0])
    rootY=findParent(connection[1])

    if rootX == rootY:
        return False
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootY] < rank[rootX]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX]+=1
    
    return True
    
print(minimumCost(4,[[1,2,3],[3,4,4]])) #O/P -> -1