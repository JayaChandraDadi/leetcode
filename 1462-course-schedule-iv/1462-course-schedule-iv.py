from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        n = len(queries)
        ans = [False]*n
        query = {}
        for i in range(n):
            u = queries[i][0]
            v = queries[i][1]
            if u not in query:
                query[u] = []
            query[u].append([v,i])
        for u,v in prerequisites:
            adj[u].append(v)
        q = deque()
        for i in range(numCourses):
            q.append(i)
            isreachable = [False]*numCourses
            while(q):
                node = q.popleft()
                for nei in adj[node]:
                    if not isreachable[nei]:
                        isreachable[nei] = True
                        q.append(nei)
            if i in query:
                arr = query[i]
                for v,index in arr:
                    if isreachable[v]==True:
                        ans[index] = True
        return ans