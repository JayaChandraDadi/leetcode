import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        pq = []
        intervals.sort()
        queries = sorted([(q,i) for i,q in enumerate(queries)])
        i = 0
        res = [-1]*len(queries)
        for q,idx in queries:
            while i<len(intervals) and intervals[i][0]<=q:
                heapq.heappush(pq,(intervals[i][1] - intervals[i][0]+1,intervals[i][1]))
                i+=1
            while pq and pq[0][1]<q:
                heapq.heappop(pq)
            if pq:
                res[idx] = pq[0][0]
        return res