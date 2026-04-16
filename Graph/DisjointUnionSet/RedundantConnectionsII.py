# You are given a directed graph edges where:
# - edges[i] = [u, v] - u is the parent of v
#
# The graph originally started as a rooted tree with n nodes:
# - exactly one root has no parent
# - every other node has exactly one parent
# - all nodes are reachable from the root
# - there are no cycles
#
# Then one extra directed edge was added.
#
# Return the edge that can be removed so the graph becomes a valid rooted tree again.
#
# If there are multiple possible answers,
# return the one that appears last in the input.
#
# ex:-
# edges = [[1,2],[1,3],[2,3]]
# O/P -> [2,3]
#
# Idea:
# - A valid rooted tree must satisfy:
#   - every node except the root has exactly one parent
#   - no directed cycle exists
#
# Since one extra directed edge was added, only two kinds of problems can happen:
#
# There are 3 cases to handle:
#
# Case 1:
# - A node has two parents, but there is no cycle
# - Then remove the later of the two parent edges
#
# Case 2:
# - A cycle exists, but no node has two parents
# - Then remove the edge that closes the cycle
#
# Case 3:
# - A node has two parents and a cycle also exists
# - Then remove the earlier of the two parent edges
#
# How to detect this:
#
# Step 1:
# - Scan all edges and track the parent of each node
# - If a node is found with two parents:
#   - store both candidate edges
#   - first parent edge  -> cand1
#   - second parent edge -> cand2
#
# Step 2:
# - Run Union-Find to check for a cycle
# - If there was a two-parent conflict:
#   - temporarily skip cand2
#   - try building the tree with all other edges
#
# Step 3:
# - Decide answer:
#   - If no cycle appears when skipping cand2:
#     - cand2 is the extra edge, return cand2
#   - If a cycle still appears when skipping cand2:
#     - cand1 is the extra edge, return cand1

def findRedundantDirectedConnection(edges):
    n = len(edges)
    parent = list(range(n + 1))
    cand1 = None
    cand2 = None
    for u, v in edges:
        if parent[v] != v:
            cand1 = [parent[v], v]   
            cand2 = [u, v]           
            break
        parent[v] = u
    uf = list(range(n + 1))
    def find(x):
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        uf[ry] = rx
        return True
    for u, v in edges:
        if cand2 and [u, v] == cand2:
            continue
        if not union(u, v):
            if not cand1:
                return [u, v]   
            return cand1        
    return cand2

print(findRedundantDirectedConnection([[1,2],[1,3],[2,3]])) #O/P -> [2,3]