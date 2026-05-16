# You are given building heights and queries.
# From building i, a person can move to building j only if:
#   i < j and heights[i] < heights[j]
#
# For each query [a, b], return the leftmost building where Alice and Bob can meet.
# Return -1 if no such building exists.
#
# ex:
# heights = [6,4,8,5,2,7]
# queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# O/P -> [2,5,-1,5,2]
#
# Idea:
# - For each query, let left = min(a, b) and right = max(a, b).
# - If a == b, they already meet at a.
# - If heights[left] < heights[right], they can meet at right.
# - Otherwise, we need the first building after right
#   with height > max(heights[a], heights[b]).
# - Process queries offline by their right index.
# - Use a monotonic decreasing stack of building indexes to the right.
# - For each delayed query, binary search the stack to find
#   the leftmost building with height greater than the needed height.
# - If found, return its index; otherwise return -1.

def leftmostBuildingQueries(heights, queries) :
    n = len(heights)
    result = [-1] * len(queries)
    waiting = [[] for _ in range(n)]
    for qi, query in enumerate(queries):
        i, j = query
        if i == j:
            result[qi] = i
            continue
        if i > j:
            i, j = j, i
        if heights[i] < heights[j]:
            result[qi] = j
        else:
            # Need first building k > j where heights[k] > heights[i]
            waiting[j].append((heights[i], qi))
    q = []
    def search(height):
        left, right = 0, len(q) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if heights[q[mid]] > height:
                ans = q[mid]
                left = mid + 1
            else:
                right = mid - 1
        return ans
    for i in range(n - 1, -1, -1):
        for height, qi in waiting[i]:
            result[qi] = search(height)
        while q and heights[q[-1]] <= heights[i]:
            q.pop()
        q.append(i)
    return result


#=============== My Solution (Memory Limit Exceeded) (Stores all the valid buildings to the right from this building in a new array ) =====================
def leftmostBuildingQueries(heights, queries):
    n = len(heights)
    max_heights = [[] for _ in range(n)]
    q = [n - 1]
    max_heights[n - 1] = q[:]
    for i in range(n - 2, -1, -1):
        if heights[i] < heights[q[-1]]:
            q.append(i)
            max_heights[i] = q[:]
        else:
            while len(q) and heights[q[-1]] <= heights[i]:
                q.pop()
            q.append(i)
            max_heights[i] = q[:]
    result = []
    def search(buildings, height, left, right):
        if left > right:
            return -1
        if left == right:
            return buildings[left] if heights[buildings[left]] > height else -1
        mid = (left + right + 1) // 2
        if heights[buildings[mid]] > height:
            return search(buildings, height, mid, right)
        else:
            return search(buildings, height, left, mid - 1)
    for query in queries:
        i, j = query
        if i == j:
            result.append(i)
            continue
        if i > j:
            i, j = j, i
        if heights[i] < heights[j]:
            result.append(j)
            continue
        valid_buildings = max_heights[j]
        ans = search(valid_buildings, heights[i], 0, len(valid_buildings) - 1)
        result.append(ans)
    return result
print(leftmostBuildingQueries([6,4,8,5,2,7],[[0,1],[0,3],[2,4],[3,4],[2,2]])) #O/P -> [2,5,-1,5,2]