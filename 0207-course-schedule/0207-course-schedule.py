from collections import deque
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
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        q = deque()
        topo = []
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while(q):
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return True if len(topo)==numCourses else False