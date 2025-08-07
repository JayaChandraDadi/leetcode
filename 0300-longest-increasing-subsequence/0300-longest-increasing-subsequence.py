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
    def lengthOfLIS(self, nums):
        n = len(nums)
        next = [0]*(n+1) 
        temp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                take =float('-inf')
                if prev==-1 or nums[prev]<nums[i]:
                    take = 1+next[i+1]
                nottake = next[prev+1]
                temp[prev+1] =  max(take,nottake)
            next = temp
        return next[0]
        