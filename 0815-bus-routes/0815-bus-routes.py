from collections import deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        q = deque()
        stops_to_routes = {}
        visited = set()
        n = len(routes)
        for i in range(n):
            for stop in routes[i]:
                if stop not in stops_to_routes:
                    stops_to_routes[stop] = []
                stops_to_routes[stop].append(i)
        if source not in stops_to_routes:
            return -1
        for route in stops_to_routes[source]:
            q.append(route)
            visited.add(route)
        min_buses = 1
        while(q):
            for i in range(len(q)):
                bus = q.popleft()
                for stop in routes[bus]:
                    if stop==target:
                        return min_buses
                    for route in stops_to_routes[stop]:
                        if route not in visited:
                            visited.add(route)
                            q.append(route)
            min_buses+=1
        return -1