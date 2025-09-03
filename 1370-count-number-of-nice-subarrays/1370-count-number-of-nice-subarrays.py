class Solution(object):
    def numberOfSubarrays(self, nums, goal):
        n = len(nums)
        oddcount = 0
        temp = []
        for i in range(n):
            if nums[i]%2==1:
                temp.append(1)
            else:
                temp.append(0)
        ct1 = 0
        l = 0
        r = 0
        sum1 = 0
        while(r<n):
            sum1+=temp[r]
            while(sum1>goal):
                sum1-=temp[l]
                l+=1
            ct1+=(r-l+1)
            r+=1
        ct2 = 0
        l = 0
        r = 0
        sum2 = 0
        if goal-1<0:
            return ct1
        while(r<n):
            sum2+=temp[r]
            while(sum2>goal-1):
                sum2-=temp[l]
                l+=1
            ct2+=(r-l+1)
            r+=1
        return ct1-ct2
