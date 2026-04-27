# You are given equations like A / B = value.
# For each query C / D, return the result if it can be found,
# otherwise return -1.0.
#
# ex:
# equations = [["a","b"],["b","c"]]
# values = [2.0, 3.0]
# queries = [["a","c"],["b","a"],["a","e"]]
# O/P -> [6.0, 0.5, -1.0]
#
#=========== My Idea===================                                           ===============Optimal Idea================
# - Build a graph where variables are nodes.                                    | - Use Weighted Union-Find.
# - For A / B = value:                                                          | - Each variable is a node.
#   - Add edge A -> B with weight value.                                        | - parent[x] stores the parent of x.
#   - Add edge B -> A with weight 1 / value.                                    | - weight[x] stores the ratio x / parent[x].
# - Use Union-Find to quickly check if two variables are connected.             | - For A / B = value:
# - For each query, if either variable is missing or not connected, return -1.0.|   - Union A and B.
# - Otherwise, use BFS to find a path from C to D.                               |   - Store enough ratio information so A / B can be calculated later.
# - Multiply edge weights along the path to get the answer.                     | - During find(x), use path compression.
#                                                                               |  - Also update weight[x] so it directly means x / root.
#                                                                               | - For each query C / D:
#                                                                               | - If either variable is missing, return -1.0.
#                                                                               | - If C and D have different roots, return -1.0.
#                                                                               | - Otherwise:
#                                                                               |       C / D = weight[C] / weight[D]
#                                                                               | - This avoids BFS for every query.
#===========================================
from collections import defaultdict,deque
def calcEquation(equations, values, queries):
    parent=defaultdict(str)
    graph=defaultdict(list) 
    result=[]
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        rootX=find(x)
        rootY=find(y)
        if rootX==rootY:
            return False
        parent[rootX]=rootY
        return True
    for i,eq in enumerate(equations):
        [x,y]=eq
        if x not in graph:
            parent[x]=x
        if y not in graph:
            parent[y]=y
        graph[x].append((values[i],y))
        graph[y].append((float(1/values[i]),x))
        union(x,y)
    for eq in queries:
        [x,y]=eq
        if x not in graph or y not in graph or find(x)!=find(y):
            result.append(-1)
            continue
        q=deque()
        q.append((x,1))
        seen=set()
        while len(q):
            curr_node,curr_val=q.popleft()
            seen.add(curr_node)
            for nei in graph[curr_node]:
                if nei[1]==y:
                    result.append(curr_val*nei[0])
                    q.clear()
                    break
                else:
                    if nei[1] not in seen:
                        q.append((nei[1],curr_val*nei[0]))
    return result
            
print(calcEquation([["a","b"],["b","c"]],[2.0, 3.0],[["a","c"],["b","a"],["a","e"]])) #O/P ->[6.0, 0.5, -1]