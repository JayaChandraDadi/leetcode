from collections import deque
class Solution(object):
    def networkDelayTime(self, times, n, k):
        timetaken = [float('inf')]*(n+1)
        queue = deque()
        queue.append([k,0])
        timetaken[k] = 0
        timetaken[0] = 0
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append([v,w])
        while(len(queue)!=0):
            node,time = queue.popleft()
            for it in adj[node]:
                neighbour = it[0]
                wt = it[1]
                if time+wt<timetaken[neighbour]:
                    timetaken[neighbour] = time+wt
                    queue.append([neighbour,time+wt])
        if max(timetaken)==float('inf'):
            return -1
        else:
            return max(timetaken)

