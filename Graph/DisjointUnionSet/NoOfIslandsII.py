# You are given:
# - an m x n grid initially filled with water
# - positions[i] = [r, c] means convert that cell into land
#
# After each addLand operation, return the number of islands.
#
# An island is formed by connecting adjacent lands:
# - up, down, left, right
#
# ex:-
# m = 3, n = 3
# positions = [[0,0],[0,1],[1,2],[2,1]]
# O/P -> [1,1,2,3]

 #m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]

def numberOfIslands(m,n,positions):
  parent=list(range(m*n))
  graph=[[-1]*n for _ in range(m) ]
  directions = [[-1,0],[0,1],[1,0],[0,-1]]
  result=0
  ans=[]
  def idx(r,c):
    return r*n+c
  def findParent(x):
    if parent[x]!=x:
      parent[x]=findParent(parent[x])
    return parent[x]
  def union(x,y):
    nonlocal result
    rx=findParent(x)
    ry=findParent(y)
    if rx!=ry:
      parent[rx]=ry
      result-=1
  for i,j in positions:
    if graph[i][j]==1:
      ans.append(result)
      continue
    result+=1
    graph[i][j]=1
    for rc,cc in directions :
      nr=i+rc
      nc=j+cc
      if nr>=0 and nr<m and nc>=0 and nc<n and graph[nr][nc]==1:
        union(idx(i,j),idx(nr,nc))
    ans.append(result)
  return ans
print(numberOfIslands(3,3,[[0,0], [0,2], [2,2], [1,2], [0,1]])) #O/P -> [1, 2, 3, 2, 1]
