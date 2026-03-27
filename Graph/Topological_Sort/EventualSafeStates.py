# There is a directed graph with n nodes labeled from 0 to n - 1.
# A node is called a terminal node if it has no outgoing edges.
# A node is called a safe node if every possible path starting from that node eventually leads to a terminal node (or another safe node)
# Return a list of all safe nodes in ascending order.

# Example:
# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
#
# Graph structure:
# 0 -> 1, 2
# 1 -> 2, 3
# 2 -> 5
# 3 -> 0
# 4 -> 5
# 5 -> []
# 6 -> []
#
# Terminal nodes: 5, 6
# Safe nodes: 2, 4, 5, 6
#
# Output -> [2,4,5,6]
from collections import defaultdict,deque
def eventualSafeNodes(graph):
    mapp=defaultdict(set);q=deque();result=[];new_map=defaultdict(set)
    for i in range(len(graph)):
        curr_node=graph[i]
        if len(curr_node) == 0:
            mapp[i]
            q.append(i)
        for neighbour in curr_node:
            new_map[i].add(neighbour)
            mapp[neighbour].add(i)
    while len(q):
        curr_node=q.popleft()
        result.append(curr_node)
        if len(mapp[curr_node])>0:
            for neighbour in mapp[curr_node]:
                new_map[neighbour].remove(curr_node)
                if len(new_map[neighbour]) == 0:
                    q.append(neighbour)
    return sorted(result)

print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) # Output -> [2,4,5,6]