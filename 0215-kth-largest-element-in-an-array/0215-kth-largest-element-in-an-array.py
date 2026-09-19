import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(pq,(nums[i]))
            while(pq and len(pq)>k):
                heapq.heappop(pq)
        return pq[0]
            