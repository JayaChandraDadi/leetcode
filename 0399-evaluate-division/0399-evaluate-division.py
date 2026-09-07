from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        q = deque()
        for i in range(len(equations)):
            u = equations[i][0]
            v = equations[i][1]
            weight = values[i]
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append([v,weight])
            adj[v].append([u,1/weight])
        ans = []
        for u,v in queries:
            if (u not in adj) or (v not in adj):
                ans.append(-1)
                continue
            if u==v:
                ans.append(1)
                continue
            q = deque()
            visited = set()
            q.append((u,1))
            visited.add(u)
            result = -1
            while(q):
                node,product_so_far = q.popleft()
                if node==v:
                    result = product_so_far
                    break
                for nei,wt in adj[node]:
                    if nei not in visited:
                        q.append((nei,wt*product_so_far))
                        visited.add(nei)
            ans.append(result)
        return ans