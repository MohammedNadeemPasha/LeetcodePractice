# You are given an array equations where each equation is a string of length 4.
#
# Each equation is of one of these two forms:
# - "a==b"  -> means both variables must be equal
# - "a!=b"  -> means both variables must be different
#
# The variables are lowercase English letters:'a' to 'z'
#
# Return True if it is possible to assign values to the variables such that all equations are satisfied.
# Otherwise return False.
#
# ex:-
# equations = ["a==b","b!=c","c==a"]
# O/P -> False
#
# equations = ["a==b","b==c","a==c"]
# O/P -> True
#
# Idea:
# - This is a Union-Find / Disjoint Set problem.
# - If two variables are equal, they must belong to the same group.
# - If two variables are not equal, they must belong to different groups.

from collections import defaultdict

def equationsPossible(equations) :
    parent=defaultdict(str)
    height=defaultdict(int)
    for i in range(len(equations)):
        if equations[i][0] not in parent:
            parent[equations[i][0]]=f'{equations[i][0]}'
            height[equations[i][0]]=0
        if equations[i][3] not in parent:
            parent[equations[i][3]]=f'{equations[i][3]}'
            height[equations[i][3]]=0
    for i in range(len(equations)):
        if equations[i][1] == '=':
            findUnion(equations[i][0],equations[i][3],parent,height)
    def findParent(node):
        if parent[node] != node:
            parent[node] = findParent(parent[node])
        return parent[node]
    
    for i in range(len(equations)):
        rootX=findParent(parent[equations[i][0]])
        rootY=findParent(parent[equations[i][3]])
        if equations[i][1] == '=':
            if rootX == rootY:
                continue
            else:
                 return False
        else:
            if rootX != rootY:
                continue
            else:
                return False
    return True

def findUnion(x,y,parent,height):
    def findParent(node):
        if parent[node] != node:
            parent[node]= findParent(parent[node])
        return parent[node]
    rootX=findParent(x)
    rootY=findParent(y)
    if rootX == rootY:
        return 
    if height[rootX]<height[rootY]:
        parent[rootX]=rootY
    elif height[rootX]>height[rootY]:
        parent[rootY]=rootX
    else:
        parent[rootX]=rootY
        height[rootY]+=1
    return

print(equationsPossible(["a==b","b!=a"])) #O/P -> False