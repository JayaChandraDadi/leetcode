class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        ans = [0]*n
        pq = []
        avaliable = []
        for i in range(n):
            heapq.heappush(avaliable,(i))
        for start,end in meetings:
            duration = end - start
            while pq and pq[0][0]<=start:
                _,room = heapq.heappop(pq)
                heapq.heappush(avaliable,(room))
            if avaliable:
                room = heapq.heappop(avaliable)
                ans[room]+=1
                heapq.heappush(pq,(end,room))
            else:
                endtime,room = heapq.heappop(pq)
                ans[room]+=1
                heapq.heappush(pq,(endtime+duration,room))
        min1 = float('-inf')
        for i in range(n):
            if min1<ans[i]:
                min1 = ans[i]
                min_index = i
        return min_index