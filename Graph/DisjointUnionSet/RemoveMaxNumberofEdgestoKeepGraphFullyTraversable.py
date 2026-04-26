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