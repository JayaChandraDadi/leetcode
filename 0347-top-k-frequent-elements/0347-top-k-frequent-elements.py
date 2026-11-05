import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pq = []
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        for el,ct in hashmap.items():
            heapq.heappush(pq,(ct,el))
        while(len(pq)>k):
            heapq.heappop(pq)
        ans = []
        for _ in range(k):
            ct,el = heapq.heappop(pq)
            ans.append(el)
        return ans