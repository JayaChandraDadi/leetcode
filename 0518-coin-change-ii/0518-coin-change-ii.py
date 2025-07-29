class Solution(object):
    def count(self,i,target,nums,dp):
        if target==0:
            return 1
        if i==0:
            if target%nums[i]==0:
                return 1
            else:
                return 0
        if dp[i][target]!=-1:
            return dp[i][target]
        nottake = self.count(i-1,target,nums,dp)
        take = 0
        if target>=nums[i]:
            take = self.count(i,target-nums[i],nums,dp)
        dp[i][target]= take+nottake
        return dp[i][target]
    def change(self, amount, nums):
        n = len(nums)
        dp = [[-1]*(amount+1) for _ in range(n)]
        return self.count(n-1,amount,nums,dp)

       
        