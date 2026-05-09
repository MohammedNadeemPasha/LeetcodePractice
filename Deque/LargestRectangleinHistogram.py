# You are given an array heights,
# where heights[i] is the height of a histogram bar.
# Each bar has width 1.
#
# Return the area of the largest rectangle in the histogram.
#
# ex:
# heights = [2,1,5,6,2,3]
# O/P -> 10
#
# Explanation:
# - The largest rectangle uses heights 5 and 6.
# - Width = 2, height = 5
# - Area = 5 * 2 = 10
#
# Idea:
# - Use a monotonic increasing stack.
# - Store indexes of bars in the stack.
# - When current height is smaller than the top stack height:
#   - Pop from stack.
#   - Treat popped height as the rectangle height.
#   - Calculate width using current index and new stack top.
#   - Update max area.
# - Add a 0 height at the end to force all bars to be processed.
# - Return max area.

from collections import deque
def largestRectangleArea(heights) :
    max_area=0
    heights.append(0)
    q=deque()
    for i,height in enumerate(heights):
        if len(q) and  height<heights[q[-1]]:
            while len(q) and heights[q[-1]]>height:
                prev_index=q.pop()
                width=0
                if not len(q):
                    width=i
                else:
                    width=i-q[-1]-1
                max_area=max(max_area,width*heights[prev_index])
        q.append(i)
    return max_area
print(largestRectangleArea([2,1,5,6,2,3])) #O/P -> 10