class Solution:
    def dfs(self,node,adj,visited,pathvisited):
        visited[node] = True
        pathvisited[node] = True
        for nei in adj[node]:
            if visited[nei]==True and pathvisited[nei]==True:
                return False
            elif visited[nei]==True and pathvisited[nei]==False:
                continue
            else:
                if self.dfs(nei,adj,visited,pathvisited)==False:
                    return False
        pathvisited[node] = False
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[]*numCourses for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        visited = [False]*numCourses
        pathvisited = [False]*numCourses
        for node in range(numCourses):
            if not visited[node]:
                if self.dfs(node,adj,visited,pathvisited)==False:
                    return False
        return True