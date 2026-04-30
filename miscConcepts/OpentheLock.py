# You are given a lock that starts at "0000".
# Each move turns one wheel up or down by 1.
# Digits wrap around, so 9 -> 0 and 0 -> 9.
#
# Some states are deadends and cannot be used.
#
# Return the minimum number of moves to reach target.
# Return -1 if it is impossible.
#
# ex:
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# O/P -> 6
#
# Idea:
# - Treat each lock state as a node in a graph.
# - From each state, generate 8 neighbors:
#   - For each of 4 wheels, turn it +1 or -1.
# - Use BFS starting from "0000" to find the shortest path.
# - Skip states that are deadends or already visited.
# - If target is found, return the number of moves.
# - If BFS finishes without reaching target, return -1.

from collections import deque
def openLock( deadends, target) :
    dead = set(deadends)
    if "0000" in dead:
        return -1
    if target == "0000":
        return 0
    queue = deque()
    queue.append(("0000", 0))
    visited = set()
    visited.add("0000")
    while queue:
        state, moves = queue.popleft()
        for i in range(4):
            digit = int(state[i])
            for change in [-1, 1]:
                new_digit = (digit + change) % 10
                new_state = (
                    state[:i] +
                    str(new_digit) +
                    state[i + 1:]
                )
                if new_state in dead:
                    continue
                if new_state in visited:
                    continue
                if new_state == target:
                    return moves + 1
                visited.add(new_state)
                queue.append((new_state, moves + 1))
    return -1

print(openLock(["0201","0101","0102","1212","2002"],"0202")) #O/P -> 6