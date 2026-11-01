class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(len(nums)+ 1)]
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        for el,ct in hashmap.items():
            buckets[ct].append(el)
        ans = []
        for i in range(n,-1,-1):
            if not buckets[i]:
                continue
            for el in buckets[i]:
                ans.append(el)
                if len(ans)==k:
                    return ans
        return ans