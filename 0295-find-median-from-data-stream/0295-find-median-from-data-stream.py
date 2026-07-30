import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.len = 0
    def addNum(self, num: int) -> None:
        self.len+=1
        if not self.max_heap or num<-self.max_heap[0]:
            heapq.heappush(self.max_heap,(-num))
        else:
            heapq.heappush(self.min_heap,(num))
        if len(self.min_heap)+1<len(self.max_heap):
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,(num))
        elif len(self.max_heap)<len(self.min_heap):
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,(-num))
    def findMedian(self) -> float:
        if (self.len)%2==0:
            return (-self.max_heap[0]+self.min_heap[0])/2
        return -self.max_heap[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()