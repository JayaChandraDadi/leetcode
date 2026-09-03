from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        hashmap = {}
        for i in range(numCourses):
            hashmap[i] = set()
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while(q):
            node = q.popleft()
            for nei in adj[node]:
                hashmap[nei].add(node)
                hashmap[nei].update(hashmap[node])
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        ans = []
        for u,v in queries:
            if u in hashmap[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans