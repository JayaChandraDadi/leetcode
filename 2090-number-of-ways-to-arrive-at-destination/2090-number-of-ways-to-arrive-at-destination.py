import heapq
class Solution(object):
    def countPaths(self, n, roads):
        dist = [float('inf')]*n
        ways = [0]*n
        ways[0] = 1
        pq = []
        mod = (10**9)+7
        heapq.heappush(pq,(0,0))
        adj = [[]*n for _ in range(n)]
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        dist[0] = 0
        while(pq):
            time,node = heapq.heappop(pq)
            for it in adj[node]:
                neighbour = it[0]
                timetaken = it[1]
                if dist[neighbour]>timetaken+time:
                    dist[neighbour] = timetaken+time
                    ways[neighbour] = ways[node]
                    heapq.heappush(pq,(dist[neighbour],neighbour))
                elif timetaken+time==dist[neighbour]:
                    ways[neighbour] = (ways[neighbour]+ways[node])%mod
        return (ways[n-1])%(mod)
