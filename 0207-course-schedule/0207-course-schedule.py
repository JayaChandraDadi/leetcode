class Solution(object):
    def dfs(self,node,vis,pathvis,adj):
        vis[node] = 1
        pathvis[node] = 1
        for neighbour in adj[node]:
            if not vis[neighbour]:
                if self.dfs(neighbour,vis,pathvis,adj):
                    return True
            if pathvis[neighbour]:
                return True
        pathvis[node] = 0
        return False
    def canFinish(self, numCourses, prerequisites):
        vis = [0]*numCourses
        pathvis = [0]*numCourses
        for i in range(numCourses):
            adj = [[] for _ in range(numCourses)]
            for u,v in prerequisites:
                adj[v].append(u)
            if not vis[i]:
                if self.dfs(i,vis,pathvis,adj):
                    return False
        return True
        