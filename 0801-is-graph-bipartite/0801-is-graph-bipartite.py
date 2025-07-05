class Solution(object):
    def dfs(self,graph,vis,node,color):
        vis[node] = color
        for neighbour in graph[node]:
            if vis[neighbour]==-1:
                if self.dfs(graph,vis,neighbour,not color)==False:
                    return False
            elif vis[neighbour]==color:
                return False
        return True


    def isBipartite(self, graph):
        n = len(graph)
        vis = [-1]*(n)
        for i in range(n):
            if vis[i]==-1:
                if self.dfs(graph,vis,i,0)==False:
                    return False
        return True
        