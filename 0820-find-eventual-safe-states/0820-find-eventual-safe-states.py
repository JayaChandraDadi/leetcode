from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        queue = deque()
        safenodes = []
        adj = [[]for _ in range(len(graph))]
        indegree = [0]*len(graph)
        for u in range(len(graph)):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u]+=1
        for i in range(len(adj)):
            if indegree[i]==0:
                queue.append(i)
                safenodes.append(i)
        while(len(queue)!=0):
            node  = queue.popleft()
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
                    safenodes.append(neighbour)
        return sorted(safenodes)

