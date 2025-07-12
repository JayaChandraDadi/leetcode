import heapq

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        # Step 1: Build adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # because it's bidirectional

        # Step 2: Dijkstra function to find shortest distances from a given city
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            min_heap = [(0, start)]  # (distance, node)
            
            while min_heap:
                current_dist, node = heapq.heappop(min_heap)
                for neighbor, weight in adj[node]:
                    if current_dist + weight < dist[neighbor]:
                        dist[neighbor] = current_dist + weight
                        heapq.heappush(min_heap, (dist[neighbor], neighbor))
            return dist

        # Step 3: Run Dijkstra from each city and count reachable cities
        min_count = n + 1
        result_city = -1

        for city in range(n):
            dist = dijkstra(city)
            reachable = sum(1 for i in range(n) if i != city and dist[i] <= distanceThreshold)
            
            # Step 4: Track city with min reachable count, break ties by larger index
            if reachable <= min_count:
                min_count = reachable
                result_city = city

        return result_city
