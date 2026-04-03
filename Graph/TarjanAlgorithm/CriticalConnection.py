

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        indegree=[0]*n
        graph=defaultdict(set)
        result=[]
        for i in range(len(connections)):
            a,b=connections[i]
            indegree[a]+=1
            indegree[b]+=1
            graph[a].add(b)
            graph[b].add(a)
        q=deque()
        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)
        while len(q):
            node= q.popleft()
            for i in graph[node]:
                graph[i].remove(node)
                indegree[i]-=1
                result.append([node,i])
        return result