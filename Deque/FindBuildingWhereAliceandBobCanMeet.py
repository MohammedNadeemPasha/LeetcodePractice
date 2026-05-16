#=============== My Solution (Memory Limit Exceeded) =====================
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
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