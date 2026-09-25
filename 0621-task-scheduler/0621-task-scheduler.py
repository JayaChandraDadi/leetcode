import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        pq = []
        hashmap = {}
        q = deque()
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 0
            hashmap[task]+=1
        for task,freq in hashmap.items():
            heapq.heappush(pq,(-freq,task))
        timestamp = 0
        while(pq or q):
            if pq:
                freq,task = heapq.heappop(pq)
                freq = abs(freq)
                freq-=1
                if freq!=0:
                    q.append([freq,timestamp+n+1,task])
                timestamp+=1
            else:
                while(timestamp<q[0][1]):
                    timestamp+=1
            while q and timestamp>=q[0][1]:
                freq,_,task = q.popleft()
                heapq.heappush(pq,(-freq,task))
        return timestamp