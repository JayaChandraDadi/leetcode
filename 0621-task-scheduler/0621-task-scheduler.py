import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        freq = {}
        q = deque()
        for i in range(len(tasks)):
            if tasks[i] not in freq:
                freq[tasks[i]] = 0
            freq[tasks[i]]+=1
        for task,ct in freq.items():
            heapq.heappush(pq,(-ct,task))
        time = 1
        while(pq or q):
            while q and time>=q[0][0]:
                _,task,ct = q.popleft()
                heapq.heappush(pq,(-ct,task))
            if pq:
                ct,task = heapq.heappop(pq)
                ct = -ct
                ct = ct-1
                if ct>0:
                    q.append((time+n+1,task,ct))
                time+=1
            else:
                while time<q[0][0]:
                    time+=1
        return time-1