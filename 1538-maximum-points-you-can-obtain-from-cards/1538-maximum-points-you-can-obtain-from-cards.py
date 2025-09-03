class Solution(object):
    def maxScore(self, nums, k):
        lsum = 0
        rsum = 0
        maxsum = 0
        n = len(nums)
        r = n-1
        for i in range(k):
            lsum+=nums[i]
        maxsum = max(maxsum,lsum)
        for j in range(k-1,-1,-1):
            lsum-=nums[j]
            rsum+=nums[r]
            r-=1
            maxsum = max(maxsum,rsum+lsum)
        return maxsum
        