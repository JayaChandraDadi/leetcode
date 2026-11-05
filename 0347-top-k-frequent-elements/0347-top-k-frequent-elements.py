import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pq = []
        n = len(nums)
        hashmap  = {}
        buckets = [[] for _ in range(n+1)]
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        for el,ct in hashmap.items():
            buckets[ct].append(el)
        ans = []
        for i in range(n,-1,-1):
            if buckets[i]==[]:
                continue
            for el in buckets[i]:
                ans.append(el)
                if len(ans)==k:
                    return ans
        return ans