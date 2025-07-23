class Solution(object):
    def maxmoney(self,n,dp,nums):
        if n==0:
            return nums[n]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        pick = nums[n] + self.maxmoney(n-2,dp,nums)
        notpick =  self.maxmoney(n-1,dp,nums)
        dp[n] = max(pick,notpick)
        return dp[n]
    def rob(self, nums):
        n = len(nums)
        dp = [-1]*n
        return self.maxmoney(n-1,dp,nums)