# You are given:
# - an n x n grid
# - each cell contains '/', '\' or ' '
#
# These slashes divide the grid into separate regions.
#
# Return the total number of regions formed.
#
# ex:-
# grid = [" /","/ "]
# O/P -> 2
#
# Idea:
# - Treat each 1 x 1 cell as 4 smaller parts: top, right, bottom, left
# - Use Union-Find to connect parts within the same cell and also connect neighboring cells.
#
# Inside each cell:
# - if the cell is ' ', connect all 4 parts
# - if the cell is '/', connect: top with left,right with bottom
# - if the cell is '\', connect: top with right, bottom with left
#
# Between cells:
# - connect bottom of current cell with top of cell below
# - connect right of current cell with left of cell to the right

def regionsBySlashes( grid ):
    n = len(grid)
    parent = list(range(4 * n * n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
    
    def idx(r, c, k):
        return 4 * (r * n + c) + k
    
    for r in range(n):
        for c in range(n):
            ch = grid[r][c]
            
            top = idx(r, c, 0)
            right = idx(r, c, 1)
            bottom = idx(r, c, 2)
            left = idx(r, c, 3)
            
            if ch == ' ':
                union(top, right)
                union(right, bottom)
                union(bottom, left)
            elif ch == '/':
                union(top, left)
                union(right, bottom)
            else: 
                union(top, right)
                union(bottom, left)
            
            if r + 1 < n:
                union(bottom, idx(r + 1, c, 0))
            
            if c + 1 < n:
                union(right, idx(r, c + 1, 3))
    
    return sum(1 for i in range(4 * n * n) if find(i) == i)