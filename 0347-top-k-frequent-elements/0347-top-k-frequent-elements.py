class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        hashmap = {}
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]]+=1
        for val,ct in hashmap.items():
            freq[ct].append(val)
        ans = []
        for i in range(n,-1,-1):
            if freq[i]==[]:
                continue
            for el in freq[i]:
                ans.append(el)
                if len(ans)==k:
                    return ans