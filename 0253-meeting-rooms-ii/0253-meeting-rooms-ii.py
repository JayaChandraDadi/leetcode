import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ct = 1
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        pq = []
        heapq.heappush(pq,(intervals[0][1]))
        for i in range(1,n):
            if intervals[i][0]<pq[0]:
                ct+=1
                heapq.heappush(pq,(intervals[i][1]))
            else:
                heapq.heappop(pq)
                heapq.heappush(pq,(intervals[i][1]))
        return ct