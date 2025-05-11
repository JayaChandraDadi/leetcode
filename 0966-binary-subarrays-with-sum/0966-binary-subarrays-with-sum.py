class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        if goal<0:
            return -1
        n = len(nums)
        sum = 0
        ct1 = 0
        l = 0
        r = 0
        while(r<n):
            sum+=nums[r]
            while(sum>goal):
                sum-=nums[l]
                l+=1
            ct1 = ct1+(r-l+1)
            r+=1
        sum = 0
        goal-=1
        if goal<0:
            return ct1
        ct2 = 0
        l = 0
        r = 0
        while(r<n):
            sum+=nums[r]
            while(sum>goal):
                sum-=nums[l]
                l+=1
            ct2 = ct2+(r-l+1)
            r+=1
        return ct1-ct2

        