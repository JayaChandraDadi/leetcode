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
        dp = [1]*(n)
        for i in range(n):
            for prev in range(i):
                if nums[prev]<nums[i]:
                    dp[i] = max(dp[i],1+dp[prev])
        return max(dp)