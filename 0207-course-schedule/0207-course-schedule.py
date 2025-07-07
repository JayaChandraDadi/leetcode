from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree = [0]*numCourses
        pathvis = [0]*numCourses
        topo = []
        queue = deque()
        for i in range(numCourses):
            adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        for i in range(numCourses):
            for neighbour in adj[i]:
                indegree[neighbour]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
                topo.append(i)
        while(len(queue)!=0):
            node = queue.popleft()
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
                    topo.append(neighbour)
        if len(topo)==numCourses:
            return True
        return False

            