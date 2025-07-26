class Solution(object):
    def subset(self,nums,target,i,dp):
        if target==0:
            return True
        if i==0:
            return (nums[0]==target)
        if dp[i][target]!=None:
            return dp[i][target]
        nottake = self.subset(nums,target,i-1,dp)
        take = False
        if target>=nums[i]:
            take = self.subset(nums,target-nums[i],i-1,dp)
        dp[i][target] = (nottake or take)
        return dp[i][target]
    def canPartition(self, nums):
        sum1 = sum(nums)
        if sum1%2==1:
            return False
        n = len(nums)
        sum1=sum1//2
        dp = [[None]*(sum1+1) for _ in range(n+1)]
        return self.subset(nums,sum1,n-1,dp)