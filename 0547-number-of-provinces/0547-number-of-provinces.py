from collections import deque
class Solution(object):
    def dfs(self,node,adj,vis):
        vis[node] = 1
        for neighbour in adj[node]:
            if vis[neighbour]==0:
                self.dfs(neighbour,adj,vis)
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        adj = [[] for _ in range(n+1)]
        ct = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
        vis = [0]*(n)
        for i in range(n):
            if vis[i]==0:
                ct+=1
                self.dfs(i,adj,vis)
        return ct
                
