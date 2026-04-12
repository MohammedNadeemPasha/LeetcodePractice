# You are given a 2D grid heights where heights[r][c] represents the height of cell (r, c).
# You start at the top-left cell (0, 0) and want to reach the bottom-right cell (rows - 1, cols - 1).

# You can move in 4 directions:
# - up, down, left, right
#
# The effort of a path is the maximum absolute difference in heights  between two consecutive cells along that path.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
#
# ex:-
# heights = [[1,2,2],[3,8,2],[5,3,5]]
# O/P -> 2
#
# Idea:
# - Use a min-heap to apply Dijkstra’s algorithm on the grid.
# - Each state stores (current_effort, row, col).
# - Moving to a neighbor has effort:
#   max(current_effort, abs(height difference))
# - Keep the minimum effort needed to reach each cell.
# - The first time we reach the bottom-right cell, that effort is the answer.

import heapq

def minimumEffortPath(heights):
    if len(heights) == 1 and len(heights[0]) ==1 :
        return 0
    seen=set()
    directions = [[-1,0],[0,1],[1,0],[0,-1]]
    heap=[(heights[0][0],0,0,0)]
    while len(heap):
        value,row,col,prev_max=heapq.heappop(heap)
        if row == len(heights)-1 and col == len(heights[0])-1:
            return prev_max
        if (row,col) in seen:
            continue
        for i,j in directions:
            if row+i >=0 and row+i<len(heights) and col+j >=0 and col+j<len(heights[0]) and (row+i,col+j) not in seen:
                temp=prev_max
                seen.add((row,col))
                height_diff = abs(heights[row+i][col+j]-heights[row][col])
                if height_diff > temp:
                    temp=height_diff
                heapq.heappush(heap,(height_diff,row+i,col+j,temp))

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # O/P -> 2
