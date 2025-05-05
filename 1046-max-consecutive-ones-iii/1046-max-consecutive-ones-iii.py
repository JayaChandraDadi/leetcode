class Solution(object):
    def longestOnes(self, nums, k):
        zeros = 0
        l = 0
        r = 0
        maxlen = 0
        while(r<len(nums)):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen
