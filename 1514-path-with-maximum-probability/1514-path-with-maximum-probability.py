import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        pq = []
        adj = [[]*n for _ in range(n)]
        for i in range(len(edges)):
            prob = succProb[i]
            u = edges[i][0]
            v = edges[i][1]
            adj[u].append([v,prob])
            adj[v].append([u,prob])
        heapq.heappush(pq,(-1.0,start_node))
        dist = [0.00000]*n
        while(pq):
            prob,node = heapq.heappop(pq)
            prob = -prob
            if node==end_node:
                return prob
            for nei,wei in adj[node]:
                new_prob = wei*prob
                if dist[nei]<new_prob:
                    dist[nei] = new_prob
                    heapq.heappush(pq,(-new_prob,nei))
        return dist[end_node]