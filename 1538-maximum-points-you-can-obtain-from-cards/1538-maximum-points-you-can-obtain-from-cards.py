class Solution(object):
    def maxScore(self, nums, k):
        lsum = 0
        rsum = 0
        maxsum = 0
        r = len(nums)-1
        for i in range(k):
            lsum+=nums[i]
        maxsum = lsum
        for i in range(k-1,-1,-1):
            lsum-=nums[i]
            rsum+=nums[r]
            r-=1
            maxsum = max(maxsum,lsum+rsum)
        return maxsum
        