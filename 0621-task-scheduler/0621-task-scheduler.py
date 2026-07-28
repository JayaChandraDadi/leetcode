import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        maxfreq = 0
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 0
            hashmap[task]+=1
            maxfreq = max(maxfreq,hashmap[task])
        maxct = 0
        for task,freq in hashmap.items():
            if freq==maxfreq:
                maxct+=1
            partations = maxfreq-1
            partations_size = n-(maxct-1)
            empty_slots = partations*partations_size
            remaining = len(tasks) - maxfreq*maxct
            idle = max(0,empty_slots - remaining)
        return len(tasks) + idle