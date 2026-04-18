# You are given: vals[i] = value of node i and edges = undirected edges of a tree
# The graph is a tree, so: it is connected, it has no cycles, there is exactly one simple path between any two nodes
#
# A good path is a path where:
# - the starting node and ending node have the same value
# - every node on the path has value less than or equal to that value
# A single node is also considered a good path.
# Return the total number of distinct good paths.
#
# ex:-
# vals = [1,3,2,1,3]
# edges = [[0,1],[0,2],[2,3],[2,4]]
# O/P -> 6
#
# Idea:
# - This is a Union-Find + sorting problem.
# - Since the path must have all values <= endpoint value, process nodes in increasing order of value.
# - When processing value x, we can safely connect nodes whose values are <= x
# - Then, among nodes with value x in the same connected component, every pair forms a good path
#========= INTIAL THOUGHTS ==========
#BFS:- For each value group, start from same-value nodes and explore outward through valid neighbors (<= current value) to see 
# which same-value nodes are reachable (works but compute heavy)
#========= OPTIMIZED APPROACH ========
#DSU:- process values in increasing order and keep merging nodes with neighbors whose values are <= current value. 
# This gradually builds connected components for the allowed graph at each threshold.
from collections import defaultdict

def numberOfGoodPaths(vals, edges) :
    parent=list(range(len(vals)))
    graph=defaultdict(list)
    values=defaultdict(list)
    result=len(vals)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(len(vals)):
        values[vals[i]].append(i)
    def findParent(node):
        if parent[node] != node:
            parent[node]=findParent(parent[node])
        return parent[node]
    def union(x,y):
        rootX=findParent(x)
        rootY=findParent(y)
        if rootX==rootY:
            return
        parent[rootX]= rootY
    for val in sorted(values):
        for node in values[val]:
            for nei in graph[node]:
                if vals[nei] <= val:
                    union(node, nei)
        count = defaultdict(int)
        for node in values[val]:
            root = findParent(node)
            count[root] += 1
        for k in count.values():
            result += k * (k - 1) // 2
    return result

print(numberOfGoodPaths([1,3,2,1,3],[[0,1],[0,2],[2,3],[2,4]])) # O/P ->6