from collections import defaultdict,deque

def minimumTime(n, relations, time) :
    indegree={x:0 for x in range(1,n+1)}
    totalTime=[0]*(n);min_result=0
    reverse_graph=defaultdict(set)
    graph=defaultdict(set)
    for courses in relations:
        [prevCourse,nextCourse] = courses
        indegree[nextCourse]+=1
        totalTime[nextCourse-1]+=time[prevCourse-1]
        reverse_graph[prevCourse].add(nextCourse)
        graph[nextCourse].add(prevCourse)
    q = deque([x for x in indegree if indegree[x] == 0])
    print(q)
    for x in range(1,n+1):
        totalTime[x-1]+=time[x-1]
    while len(q):
        minimum=float('inf')
        count=0
        minimum_nodes=[]
        for x in q:
            print(totalTime)
            if totalTime[x]==minimum:
                minimum_nodes.append(x)
            if totalTime[x]<minimum:
                minimum_nodes=[x]
                minimum=totalTime[x]
        min_result+=minimum
        print(minimum_nodes)
        for nodes in minimum_nodes:
            for neighbours in reverse_graph[nodes]:
                totalTime[neighbours-1]-=minimum
                if totalTime[neighbours-1]== 0:
                    if len(reverse_graph[nodes]):
                        reverse_graph[nodes].remove(neighbours)
                    q.append(neighbours)
                    count+=1
        new_q = deque()
        for i in range(len(q) - count):
            totalTime[q[i]] -= minimum
            if totalTime[q[i]] != 0:
                new_q.append(q[i])
        for i in range(len(q) - count, len(q)):
            new_q.append(q[i])
        q = new_q
    return min_result
            
            