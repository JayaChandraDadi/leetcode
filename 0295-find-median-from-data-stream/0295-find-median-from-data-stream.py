import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
    def addNum(self, num: int) -> None:
        if not self.minheap or self.minheap[0]<num:
            heapq.heappush(self.minheap,(num))
        else:
            heapq.heappush(self.maxheap,(-num))
        if len(self.minheap)>len(self.maxheap)+1:
            el = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,(-el))
        elif len(self.minheap)<len(self.maxheap):
            el = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,(el))
    def findMedian(self) -> float:
        if (len(self.minheap)+len(self.maxheap))%2==0:
            return (self.minheap[0] + -self.maxheap[0])/2
        else:
            return self.minheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()