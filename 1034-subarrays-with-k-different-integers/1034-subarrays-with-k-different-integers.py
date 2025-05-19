class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        l = 0
        r = 0
        ct1 = 0
        mpp = {}
        while(r<len(nums)):
            if nums[r] not in mpp:
                mpp[nums[r]] = 1
            else:
                mpp[nums[r]]+=1
            while(len(mpp)>k):
                mpp[nums[l]]-=1
                if mpp[nums[l]]==0:
                    del mpp[nums[l]]
                l+=1
            ct1+=(r-l+1)
            r+=1
        l = 0
        r = 0
        ct2 = 0
        mpp = {}
        while(r<len(nums)):
            if nums[r] not in mpp:
                mpp[nums[r]] = 1
            else:
                mpp[nums[r]]+=1
            while(len(mpp)>k-1):
                mpp[nums[l]]-=1
                if mpp[nums[l]]==0:
                    del mpp[nums[l]]
                l+=1
            ct2+=(r-l+1)
            r+=1
        return ct1-ct2
        

