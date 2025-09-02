class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        n= len(nums)
        ct1 = 0
        l = 0
        r = 0
        sum1 = 0
        while(r<n):
            sum1+=nums[r]
            while(sum1>goal):
                sum1-=nums[l]
                l+=1
            ct1 = ct1 + (r-l+1)
            r+=1
        sum2 = 0
        l = 0
        r = 0
        ct2 = 0
        if goal-1<0:
            return ct1
        while(r<n):
            sum2+=nums[r]
            while(sum2>goal-1):
                sum2-=nums[l]
                l+=1
            ct2 = ct2 + (r-l+1)
            r+=1
        return ct1-ct2





        