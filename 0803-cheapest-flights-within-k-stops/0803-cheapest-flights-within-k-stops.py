from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')]*n
        adj = [[] for i in range(n)]
        for u,v,w in flights:
            adj[u].append([v,w])
        queue = deque()
        queue.append([0,src,0])
        while(len(queue)!=0):
            stops,node,cost = queue.popleft()
            if stops>k:
                continue
            for it in adj[node]:
                neighbour = it[0]
                wt = it[1]
                if wt+cost<dist[neighbour] and stops<=k:
                    dist[neighbour] = wt+cost
                    queue.append([stops+1,neighbour,wt+cost])
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]




        
        