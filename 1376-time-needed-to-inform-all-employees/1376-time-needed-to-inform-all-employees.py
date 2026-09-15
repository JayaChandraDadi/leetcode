from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                adj[manager[i]].append(i)
        q = deque()
        q.append((headID,informTime[headID]))
        total = 0
        while(q):
            node,time = q.popleft()
            total = max(total,time)
            for nei in adj[node]:
                q.append((nei,time + informTime[nei]))
        return total