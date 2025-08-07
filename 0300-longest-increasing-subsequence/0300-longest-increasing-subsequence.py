class Solution(object):
    def length(self,i,prev,nums,n,dp):
        if i==n:
            return 0
        take =float('-inf')
        if dp[i][prev+1]!=-1:
            return dp[i][prev+1]
        if prev==-1 or nums[prev]<nums[i]:
            take = 1+self.length(i+1,i,nums,n,dp)
        nottake = self.length(i+1,prev,nums,n,dp)
        dp[i][prev+1] =  max(take,nottake)
        return dp[i][prev+1]
    def lowerbound(self,low,high,el,arr):
        while(low<=high):
            mid = (low+high)//2
            if arr[mid]<el:
                low = mid+1
            else:
                index = mid
                high = mid-1
        return index
    def lengthOfLIS(self, nums):
        n = len(nums)
        temp = []
        temp.append(nums[0])
        length = 1
        for i in range(1,n):
            if temp[-1]<nums[i]:
                temp.append(nums[i])
                length+=1
            else:
                index = self.lowerbound(0,len(temp)-1,nums[i],temp)
                temp[index] = nums[i]
        return length