class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        l = 0
        r = 0
        ct1 = 0
        hashmap = {}
        while(r<len(nums)):
            if nums[r] not in hashmap:
                hashmap[nums[r]] = 0
            hashmap[nums[r]]+=1
            if len(hashmap)>k:
                while(len(hashmap)>k):
                    hashmap[nums[l]]-=1
                    if hashmap[nums[l]]==0:
                        hashmap.pop(nums[l])
                    l+=1
            ct1+=(r-l+1)
            r+=1
        l = 0
        r = 0
        ct2 = 0
        hashmap = {}
        while(r<len(nums)):
            if nums[r] not in hashmap:
                hashmap[nums[r]] = 0
            hashmap[nums[r]]+=1
            if len(hashmap)>k-1:
                while(len(hashmap)>k-1):
                    hashmap[nums[l]]-=1
                    if hashmap[nums[l]]==0:
                        hashmap.pop(nums[l])
                    l+=1
            ct2+=(r-l+1)
            r+=1
        return ct1-ct2
        
                

        