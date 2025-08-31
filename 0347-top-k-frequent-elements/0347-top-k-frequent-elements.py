class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        hashmap = {}
        freq = [[] for _ in range(n+1)]
        for n1 in nums:
            if n1 not in hashmap:
                hashmap[n1] = 1
            else:
                hashmap[n1]+=1
        for element,ct in hashmap.items():
            freq[ct].append(element)
        res = []
        for i in range(len(freq)-1,-1,-1):
            if not freq[i]:
                continue
            for element in freq[i]:
                res.append(element)
                if len(res)==k:
                    return res

         
            
