# Given n courses labeled from 1 to n, along with a list of prerequisite relations and an array time,
# return the minimum number of months required to complete all courses.
# Each relation [a, b] means course a must be completed before course b.
# time[i] represents the number of months required to complete course (i+1).
# You can:
# - Start a course anytime after completing its prerequisites.
# - Take multiple courses simultaneously.
#
# The input guarantees that all courses can be completed (i.e., no cycles).
#
# ex:- n = 3, relations = [[1,3],[2,3]], time = [3,2,5] ; O/P -> 8
from collections import defaultdict, deque


def minimumTime(n, relations, time) :
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for u, v in relations:
        graph[u].append(v)
        indegree[v] += 1

    dp = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = time[i - 1]
            q.append(i)

    while q:
        u = q.popleft()
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + time[v - 1])
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return max(dp)

print(minimumTime(3,[[1,3],[2,3]],[3,2,5])) #O/P -> 8