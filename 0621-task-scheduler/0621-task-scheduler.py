import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxfreq = 0
        freq = {}
        for i in range(len(tasks)):
            if tasks[i] not in freq:
                freq[tasks[i]] = 0
            freq[tasks[i]]+=1
            maxfreq = max(maxfreq,freq[tasks[i]])
        maxct = 0
        for task,ct in freq.items():
            if ct==maxfreq:
                maxct+=1
            partation_size = n-(maxct-1)
            partations = maxfreq - 1
            empty_slots = partations*partation_size
            remaining_tasks = len(tasks) - maxfreq*maxct
            idlesots = max(0,empty_slots-remaining_tasks)
        return len(tasks) + idlesots