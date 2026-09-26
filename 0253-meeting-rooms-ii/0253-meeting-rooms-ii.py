import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        pq = []
        rooms = 0
        intervals.sort(key=lambda x:x[0])
        for start,end in intervals:
            if not pq or start<pq[0]:
                rooms+=1
            else:
                heapq.heappop(pq)
            heapq.heappush(pq,(end))
        return rooms
