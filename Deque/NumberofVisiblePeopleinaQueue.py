# You are given heights of people standing in a queue.
#
# For each person, return how many people they can see to their right.
#
# A person can see shorter people until a taller person blocks the view.
# They can also see the first taller person, but nobody behind that taller person.
#
# ex:
# heights = [10,6,8,5,11,9]
# O/P -> [3,1,2,1,1,0]
#
# Idea:
# - Use a monotonic decreasing stack from right to left.
# - The stack stores people to the right that may be visible.
# - While the top of stack is shorter than current person:
#   - Current person can see them.
#   - Pop them because current person blocks them for people on the left.
# - If stack is still not empty:
#   - Current person can see the first taller person.
# - Push current height into the stack.
# - Return the answer array.

def canSeePersonsCount(heights):
    n = len(heights)
    ans = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] < heights[i]:
            stack.pop()
            ans[i] += 1
        if stack:
            ans[i] += 1
        stack.append(heights[i])
    return ans
print(canSeePersonsCount([10,6,8,5,11,9])) #O/P -> [3, 1, 2, 1, 1, 0]