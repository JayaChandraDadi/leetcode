class Solution(object):
    def dfs(self, adj, node, vis, pathvis, stack):
        vis[node] = 1
        pathvis[node] = 1
        for neighbour in adj[node]:
            if vis[neighbour] == 0:
                if self.dfs(adj, neighbour, vis, pathvis, stack):
                    return True
            elif pathvis[neighbour] == 1:
                return True  
        pathvis[node] = 0
        stack.append(node)
        return False

    def findOrder(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)

        vis = [0] * numCourses
        pathvis = [0] * numCourses
        stack = []

        for i in range(numCourses):
            if vis[i] == 0:
                if self.dfs(adj, i, vis, pathvis, stack):
                    return []  
        return stack[::-1]  
