from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[]*numCourses for _ in range(numCourses)]
        ans = []
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while(q):
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans if len(ans)==numCourses else []