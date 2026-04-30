# You are given bus routes, where routes[i] contains all stops for bus i.
# Starting at source, return the minimum number of buses needed to reach target.
# Return -1 if it is impossible.
#
# ex:
# routes = [[1,2,7],[3,6,7]]
# source = 1
# target = 6
# O/P -> 2
#
# Idea:
# - Build a map from each stop to the buses that visit it.
# - Use BFS starting from source.
# - Each BFS level represents taking one more bus.
# - From the current stop, try every bus that stops there.
# - For each unused bus, visit all stops on that bus route.
# - If target is reached, return buses_taken.
# - Use a set to avoid taking the same bus again.
# - If BFS ends without reaching target, return -1.

from collections import defaultdict,deque
def numBusesToDestination(routes, source, target) :
    stop_graph=defaultdict(list)
    route_graph=defaultdict(list)
    if source == target:
        return 0
    for i,route in enumerate(routes):
        route_graph[i].append(route)
        for stops in route:
            stop_graph[stops].append(i)
    if source not in stop_graph or target not in stop_graph:
        return -1
    seen=set()
    start=(source,0,seen)
    q=deque()
    q.append(start)
    while len(q):
        curr_stop,buses_taken,seen_routes=q.popleft()
        if curr_stop == target:
            return buses_taken
        for next_routes in stop_graph[curr_stop]:
            if next_routes in seen_routes:
                continue
            else:
                seen_routes.add(next_routes)
                for next_stops in route_graph[next_routes][0]:
                    q.append((next_stops,buses_taken+1,seen_routes))
    return -1