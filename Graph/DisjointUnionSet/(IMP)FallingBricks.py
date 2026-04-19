# You are given:
# - grid[r][c] = 1 means a brick, 0 means empty
# - hits[i] = [r, c] means remove that brick if it exists
#
# A brick is stable if:
# - it is connected to the top row, or
# - it is connected to another stable brick in 4 directions
#
# After each hit, unstable bricks fall and disappear.
#
# Return an array where result[i] is the number of bricks that fall after the i-th hit.
#
# ex:-
# grid = [[1,0,0,0],[1,1,1,0]],hits = [[1,0]],O/P -> [2]
#
# Idea:
# - Removing bricks forward is hard, because many bricks may fall each time.
# - So process hits in reverse.
# - First, remove all hit positions from the grid.
# - Build Union-Find on the remaining bricks.
# - Add one extra virtual top node to represent all stable bricks.
# - Any brick in the top row is connected to this top node.

# DSU is good at merging components, not splitting them.
# In the forward direction, each hit is a deletion:
# - removing one brick can break one connected component into multiple pieces
# - some pieces remain stable, some become floating
# - to know that, we would need to re run dsu on entire graph
# DSU cannot efficiently undo unions or split a set apart.

def hitBricks( grid, hits) :
    m, n = len(grid), len(grid[0])
    roof = m * n
    parent = list(range(m * n + 1))
    size = [1] * (m * n + 1)
    def idx(r, c):
        return r * n + c
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        parent[rx] = ry
        size[ry] += size[rx]
    original = [row[:] for row in grid]
    for r, c in hits:
        if grid[r][c] == 1:
            grid[r][c] = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] != 1:
                continue
            if r == 0:
                union(idx(r, c), roof)
            if r > 0 and grid[r - 1][c] == 1:
                union(idx(r, c), idx(r - 1, c))
            if c > 0 and grid[r][c - 1] == 1:
                union(idx(r, c), idx(r, c - 1))
    ans = [0] * len(hits)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(len(hits) - 1, -1, -1):
        r, c = hits[i]
        if original[r][c] == 0:
            ans[i] = 0
            continue
        before = size[find(roof)]
        grid[r][c] = 1
        node = idx(r, c)
        if r == 0:
            union(node, roof)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                union(node, idx(nr, nc))
        after = size[find(roof)]
        ans[i] = max(0, after - before - 1)
    return ans
print(hitBricks([[1,0,0,0],[1,1,1,0]],[[1,0]])) #O/P -> [2]