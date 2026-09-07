from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        q = deque()
        degree = [0]*n
        adj = [[] for _ in range(n)]
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        remaining = n
        for i in range(n):
            if degree[i]==1:
                q.append(i)
        while(remaining>2):
            layer_length = len(q)
            remaining-=layer_length
            for _ in range(layer_length):
                node = q.popleft()
                for nei in adj[node]:
                    degree[nei]-=1
                    if degree[nei]==1:
                        q.append(nei)
        return list(q)