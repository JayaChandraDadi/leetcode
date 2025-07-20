class Solution(object):
    def dfs(self,adj,vis,tin,low,bridges,node,parent,timer):
        vis[node] = 1
        tin[node] = timer
        low[node] = timer
        timer+=1
        for it in adj[node]:
            if it==parent:
                continue
            if vis[it]==0:
                self.dfs(adj,vis,tin,low,bridges,it,node,timer)
                low[node] = min(low[node],low[it])
                if tin[node]<low[it]:
                    bridges.append([node,it])
            else:
                low[node] = min(low[node],low[it])
    def criticalConnections(self, n, connections):
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0]*n
        tin = [0]*n
        low = [0]*n
        bridges = []
        self.dfs(adj,vis,tin,low,bridges,0,-1,1)
        return bridges
        