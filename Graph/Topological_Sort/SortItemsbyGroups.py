from collections import defaultdict,deque
def sortItems( n, m, group, beforeItems):
    group_map={}
    for i in range(len(group)):
        if group[i] not in group_map:
            group_map[group[i]]=[i]
        else:
            group_map[group[i]].append(i)
    group_indegree=defaultdict(int)
    graph={}
    indegree=[0]*(n)
    for index,items in enumerate(beforeItems):
        for i in items:
            indegree[index]+=1
            if group[i] !=group[index]:
                group_indegree[index]+=1
                if i not in group_indegree:
                    group_indegree[i]=0
                if group[i] in graph:
                    graph[group[i]].append(group[index])
                else:
                    graph[group[i]]=[group[index]]


        