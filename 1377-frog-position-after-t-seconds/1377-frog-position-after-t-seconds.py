from collections import deque
class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        q = deque()
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q.append((0,1,1.0))
        visited = [False]*(n+1)
        visited[1] = True
        while(q):
            time,node,current_prob = q.popleft()
            avaliable = []
            for nei in adj[node]:
                if not visited[nei]:
                    avaliable.append(nei)
            if node==target:
                if time==t or not avaliable:
                    return current_prob
                return 0.0
            if not avaliable:
                continue
            if time==t:
                continue
            new_prob = 1/len(avaliable)
            for nei in avaliable:
                visited[nei] = True
                q.append((time+1,nei,current_prob*new_prob))
        return 0.0
        