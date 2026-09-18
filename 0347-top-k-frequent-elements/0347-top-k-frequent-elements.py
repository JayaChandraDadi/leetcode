import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        for el,freq in hashmap.items():
            heapq.heappush(pq,(freq,el))
        while pq and len(pq)>k:
            heapq.heappop(pq)
        ans = []
        while(pq):
            freq,el = heapq.heappop(pq)
            ans.append(el)
        return ans