# You are given a weighted undirected connected graph with n nodes.
# edges[i] = [u, v, weight]
#
# Return two lists:
# 1. Critical edges:
#    Removing this edge makes the MST weight increase or makes MST impossible.
# 2. Pseudo-critical edges:
#    This edge can be part of some MST, but is not required in every MST.
#
# ex:
# n = 5
# edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# O/P -> [[0,1],[2,3,4,5]]
#
# Idea:
# - Add original index to each edge, then sort edges by weight.
# - Use Kruskal's algorithm to find the original MST weight.
# - For each edge:
#   - Skip the edge and build MST again.
#     If MST weight increases, the edge is critical.
#   - Force the edge first and build MST again.
#     If MST weight stays the same, the edge is pseudo-critical.
# - Return [critical, pseudo_critical].

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.count -= 1
        return True
from typing import List
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed_edges = []
        for i, (u, v, w) in enumerate(edges):
            indexed_edges.append((u, v, w, i))
        indexed_edges.sort(key=lambda x: x[2])
        def kruskal(skip_edge_index=-1, force_edge=None):
            dsu = DSU(n)
            total = 0
            if force_edge is not None:
                u, v, w, idx = force_edge
                if dsu.union(u, v):
                    total += w
            for u, v, w, idx in indexed_edges:
                if idx == skip_edge_index:
                    continue
                if dsu.union(u, v):
                    total += w
            if dsu.count != 1:
                return float("inf")
            return total
        original_mst_weight = kruskal()
        critical = []
        pseudo_critical = []
        for edge in indexed_edges:
            u, v, w, idx = edge
            weight_without_edge = kruskal(skip_edge_index=idx)
            if weight_without_edge > original_mst_weight:
                critical.append(idx)
                continue
            weight_with_edge = kruskal(force_edge=edge)
            if weight_with_edge == original_mst_weight:
                pseudo_critical.append(idx)
        return [critical, pseudo_critical]
    
sol=Solution()
print(sol.findCriticalAndPseudoCriticalEdges(5,[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])) # O/P -> [[0, 1], [2, 3, 4, 5]]