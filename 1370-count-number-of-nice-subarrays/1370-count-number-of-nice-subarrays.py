class Solution(object):
    def numberOfSubarrays(self, nums, goal):
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i]%2)
        if goal<0:
            return -1
        n = len(temp)
        sum = 0
        ct1 = 0
        l = 0
        r = 0
        while(r<n):
            sum+=temp[r]
            while(sum>goal):
                sum-=temp[l]
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
            sum+=temp[r]
            while(sum>goal):
                sum-=temp[l]
                l+=1
            ct2 = ct2+(r-l+1)
            r+=1
        return ct1-ct2
