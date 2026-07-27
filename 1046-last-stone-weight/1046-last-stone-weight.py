import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        n = len(stones)
        for i in range(n):
            heapq.heappush(pq,(-stones[i]))
        while(len(pq)>1):
            y = abs(heapq.heappop(pq))
            x = abs(heapq.heappop(pq))
            if x==y:
                continue
            heapq.heappush(pq,-(y-x))
        return abs(pq[0]) if pq else 0