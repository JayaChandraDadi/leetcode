class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        freq = [[] for _ in range(n+1)]
        for el,ct in hashmap.items():
            freq[ct].append(el)
        res = []
        for i in range(n,-1,-1):
            for el in freq[i]:
                res.append(el)
                if len(res)==k:
                    return res




        