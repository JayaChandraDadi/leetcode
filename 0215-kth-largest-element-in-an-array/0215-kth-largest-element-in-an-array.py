import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(pq,(-nums[i]))
        for i in range(k):
            el = heapq.heappop(pq)
        return -el
