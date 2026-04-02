# There are n items and m groups. Each item belongs to at most one group, where group[i] is the group of the i-th item, 
# or -1 if it belongs to no group.Both items and groups are zero-indexed, and some groups may have no items.
# You are given dependencies where beforeItems[i] is a list of items that must come before item i in the final ordering.
# Return a list of items sorted such that:
# 1) All items in the same group appear next to each other.
# 2) All dependency constraints are satisfied.
# If multiple valid answers exist, return any one of them.
# If no valid ordering exists, return an empty list.
#
# ex:- n = 8, m = 2
# group = [-1,-1,1,0,0,1,0,-1]
# beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# O/P -> [any valid ordering satisfying constraints, e.g. one possible answer]
from collections import defaultdict, deque

def sortItems( n, m, group, beforeItems):
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    group_indegree = defaultdict(int)
    group_graph = defaultdict(list)
    group_members = defaultdict(list)

    item_graph = defaultdict(list)
    item_indegree = defaultdict(int)
    result = []

    for i in range(m):
        group_indegree[i] = 0

    for index, item in enumerate(group):
        group_members[item].append(index)
    for index in range(n):
        for prev in beforeItems[index]:
            if group[prev] != group[index]:
                group_graph[group[prev]].append(group[index])
                group_indegree[group[index]] += 1
            else:
                item_graph[prev].append(index)
                item_indegree[index] += 1

    q = deque()
    for i in range(m):
        if group_indegree[i] == 0:
            q.append(i)

    if len(q) == 0:
        return []

    while q:
        current_group = q.popleft()
        item_q = deque()
        group_result = []
        local_indegree = {}
        for item in group_members[current_group]:
            local_indegree[item] = item_indegree[item]

        for item in group_members[current_group]:
            if local_indegree[item] == 0:
                item_q.append(item)

        while item_q:
            curr_item = item_q.popleft()
            group_result.append(curr_item)

            for neighbour in item_graph[curr_item]:
                local_indegree[neighbour] -= 1
                if local_indegree[neighbour] == 0:
                    item_q.append(neighbour)

        if len(group_result) != len(group_members[current_group]):
            return []

        result.extend(group_result)

        for neighbour in group_graph[current_group]:
            group_indegree[neighbour] -= 1
            if group_indegree[neighbour] == 0:
                q.append(neighbour)

    if len(result) != n:
        return []

    return result

print(sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]])) # O/P -> [6, 3, 4, 5, 2, 0, 7, 1]