from collections import deque
class Solution:
    def can(self,mincost,graph,topo,online,k,n):
        dist = [float('inf')]*n
        dist[0] = 0
        for node in topo:
            if dist[node]==float('inf'):
                continue
            if dist[node]>k:
                continue
            for nei,cost in graph[node]:
                if cost<mincost:
                    continue
                if online[nei]==False:
                    continue
                cost_so_far = dist[node] + cost
                if cost_so_far<dist[nei] and cost_so_far<=k:
                    dist[nei] = cost_so_far
        return dist[n-1]<=k
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        q = deque()
        graph = [[]*(n) for _ in range(n)]
        maxcost = float('-inf')
        indegree = [0]*n
        for u,v,cost in edges:
            graph[u].append([v,cost])
            indegree[v]+=1
            maxcost = max(maxcost,cost)
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        topo = []
        while(q):
            node = q.popleft()
            topo.append(node)
            for nei,cost in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        low = 0
        high = maxcost
        ans = -1
        while(low<=high):
            mid = (low + high)//2
            if self.can(mid,graph,topo,online,k,n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans