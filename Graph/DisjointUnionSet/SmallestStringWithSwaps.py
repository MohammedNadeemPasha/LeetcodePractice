# You are given a string s and a list of index pairs
# Each pair [a, b] means:
# - the characters at index a and index b can be swapped
# You can perform these swaps any number of times.
# Return the lexicographically smallest string possible after using
# any number of allowed swaps.
#
# ex:-
# s = "dcab"
# pairs = [[0,3],[1,2]]
# O/P -> "bacd"
#
# s = "dcab"
# pairs = [[0,3],[1,2],[0,2]]
# O/P -> "abcd"
#
# Idea:
# - This is a Union-Find / connected components problem.
# - If two indices can be swapped directly or indirectly,
#   they belong to the same connected component.

from collections import defaultdict
def smallestStringWithSwaps(s, pairs) :
    parent=list(range(len(s)))
    graph=defaultdict(set)
    result=list(s)
    def uf(node):
        if parent[node]!=node:
            parent[node]=uf(parent[node])
        return parent[node]
    def union(x,y):
        rootX=uf(x)
        rootY=uf(y)
        if rootX == rootY:
            return
        else:
            parent[rootY] = rootX
    for i in range(len(pairs)):
        union(pairs[i][0],pairs[i][1])
    
    for i in range(len(pairs)):
        [a,b]=pairs[i]
        uf(a)
        uf(b)
        graph[parent[a]].add(a)
        graph[parent[b]].add(b)
    for i in graph:
        indices = sorted(graph[i])
        chars = []
        for j in indices:
            chars.append(s[j])
        chars.sort()
        for k in range(len(indices)):
            result[indices[k]] = chars[k]
    return ''.join(result)
print(smallestStringWithSwaps('dcab',[[0,3],[1,2]])) #O/P -> 'bacd'