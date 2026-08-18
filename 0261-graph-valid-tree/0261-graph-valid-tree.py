class Solution:
    def dfs(self,node,adj,parent,visited):
        visited[node] = True
        for nei in adj[node]:
            if visited[nei]==True and nei!=parent:
                return False
            elif visited[nei]==True and nei==parent:
                continue
            else:
                if self.dfs(nei,adj,node,visited)==False:
                    return False
        return True
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[]*n for _ in range(n)]
        visited = [False]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        if self.dfs(0,adj,-1,visited)==False:
            return False
        for i in range(n):
            if visited[i]==False:
                return False
        return True
