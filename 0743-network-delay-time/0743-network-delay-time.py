import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False]*(n+1)
        adj = [[] for _ in range(n+1)]
        for u,v,time in times:
            adj[u].append([v,time])
        pq = []
        heapq.heappush(pq,(0,k))
        node_time = [float('inf')]*(n+1)
        node_time[k] = 0
        while(pq):
            timetaken,node = heapq.heappop(pq)
            for nei,time in adj[node]:
                new_time = timetaken+time
                if new_time<node_time[nei]:
                    node_time[nei] = new_time
                    heapq.heappush(pq,(time+timetaken,nei))
        ans = max(node_time[1:])
        return -1 if ans==float('inf') else ans