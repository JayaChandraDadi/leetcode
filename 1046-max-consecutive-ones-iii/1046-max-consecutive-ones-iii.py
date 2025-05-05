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
                while(zeros>k):
                    if nums[l]==0:
                        zeros-=1
                    l+=1
            length = r-l+1
            maxlen = max(maxlen,length)
            r+=1
        return maxlen
