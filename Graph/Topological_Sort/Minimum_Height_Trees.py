# Given a tree with n nodes labeled from 0 to n - 1, return all possible roots of the tree that produce minimum height trees (MHTs).
# A tree is an undirected graph with no cycles.The height of a rooted tree is the number of edges on the longest downward path 
# from the root to a leaf. You can return the answer in any order.

# Example 1:
# n = 4
# edges = [[1,0],[1,2],[1,3]]
# Tree structure:
#       1
#     / | \
#    0  2  3
# Output -> [1]

# Example 2:
# n = 6
# edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]
# Tree structure:
#         3
#      / / \ \
#     0 1  2  4
#               \
#                5
# Output -> [3,4]

from collections import defaultdict, deque

def findMinHeightTrees( n, edges):
    if n == 1:
        return [0]

    graph = defaultdict(set)

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    leaves = deque()
    for node in range(n):
        if len(graph[node]) == 1:
            leaves.append(node)

    remaining = n

    while remaining > 2:
        leaf_count = len(leaves)
        remaining -= leaf_count

        for _ in range(leaf_count):
            leaf = leaves.popleft()
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)

    return list(leaves)

print(findMinHeightTrees(6,[[0,3],[1,3],[2,3],[4,3],[5,4]]))