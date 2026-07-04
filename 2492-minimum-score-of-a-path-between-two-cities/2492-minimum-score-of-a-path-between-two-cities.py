from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[]*(n+1) for _ in range(n+1)]
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        q = deque()
        q.append(1)
        visited = [False]*(n+1)
        visited[1] = True
        ans = float('inf')
        while(q):
            node = q.popleft()
            for nei,wt in adj[node]:
                ans = min(ans,wt)
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
        return ans