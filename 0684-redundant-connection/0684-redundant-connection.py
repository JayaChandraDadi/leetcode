class Solution:
    def dfs(self,node,par,adj,visited,parent):
        visited[node] = True
        for nei in adj[node]:
            if visited[nei]==True and nei!=par:
                if self.cycle_start==-1:
                    self.cycle_start = nei
                parent[nei] = node
                return True
            elif visited[nei]==False:
                parent[nei] = node
                if self.dfs(nei,node,adj,visited,parent)==True:
                    return True
        return False
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.cycle_start = -1
        parent = [0]*(n+1)
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n+1):
            parent[i] = i
        visited = [False]*(n+1)
        self.dfs(1,-1,adj,visited,parent)
        cycle_nodes = set()
        node = self.cycle_start
        while(True):
            cycle_nodes.add(node)
            node = parent[node]
            if node in cycle_nodes:
                break
        for i in range(n-1,-1,-1):
            if edges[i][0] in cycle_nodes and edges[i][1] in cycle_nodes:
                return edges[i]